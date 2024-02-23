from django import forms 
from first_app.models import MyModel, NewModel

from django.forms.widgets import NumberInput
import datetime




BIRTH_YEARS = ['1998', '1999', '2000']


FAV_COLORS = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ('dark green', 'Dark Green'),
]

FAV_SPORTS = [
    ('cricket',"Cricket"),
    ('football',"Football"),
    ('badminton',"Badminton"),
    ('hockey',"Hockey"),
]


class StudentForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':10}))
    email = forms.EmailField(label="Please Enter your email address")
    agree = forms.BooleanField(initial=True)
    date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    birth_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEARS))
    value = forms.DecimalField(required=False)

    message = forms.CharField(max_length=10)

    first_name = forms.CharField(initial="Your First Name")   
    todays_date = forms.DateField(initial=datetime.date.today)

    fav_color = forms.ChoiceField(widget=forms.RadioSelect ,choices=FAV_COLORS)
    fav_sports = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAV_SPORTS, label="Select your Favorite Sports")
    fav_sports2 = forms.MultipleChoiceField(choices=FAV_SPORTS, label="Select your Favorite Sports")



    # geeks
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    roll_number = forms.IntegerField(help_text="Enter roll number")
    password = forms.CharField(widget=forms.PasswordInput)


class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields ='__all__'


class NewForm(forms.ModelForm):
    class Meta:
        model = NewModel
        fields = '__all__'
        