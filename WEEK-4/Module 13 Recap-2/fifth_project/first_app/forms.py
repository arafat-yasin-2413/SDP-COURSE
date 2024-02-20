from django import forms
from django.core import validators

# widgets = fields to html input
class contactForm(forms.Form):
    name = forms.CharField(label="Name",initial="Rahim",   help_text="Text Limit can't exceed 70 characters", required=False, widget=forms.Textarea)
    
    
    # birthday = forms.CharField(widget=forms.DateInput(attrs={'type':'date'}))

    # appointment = forms.CharField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))

    # file = forms.FileField()
    # email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    
    CHOICES = [('S','Small'),('M',"Medium"),('L',"Large")]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    meat = [('P','Pepperoni'),('M',"Mushroom"),('B',"Beef")]
    pizza = forms.MultipleChoiceField(choices=meat, widget=forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#     name = forms.CharField(widget= forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)

    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname)  < 10:
    #         raise forms.ValidationError('Name Must be at least 10 characters')
    #     return valname
    
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Email must contain .com ')
    #     return valemail

    # def clean(self):
    #     cleaned_data = super().clean()

    #     valname = cleaned_data['name']
    #     valemail = cleaned_data['email']

    #     if len(valname) < 10:
    #         raise forms.ValidationError('Name must be at least 10 characters')
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Email must contain .com ')
        
def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError('Length must be at least 10 chars')

class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(10,message="Enter a name having at least 10 chars")])

    text = forms.CharField(widget=forms.TextInput, validators=[len_check])

    email = forms.CharField(widget=forms.EmailInput, validators= [validators.EmailValidator(message="Enter a valid Email")])

    age = forms.IntegerField(validators= [validators.MaxValueValidator(34,message="Maximum age is 34"), validators.MinValueValidator(24,message="Minumum age is 24")])

    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','jpg'], message="File Extension must be ended with .pdf or .jpg")])


class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_pass= forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = cleaned_data['password']
        val_conf_pass = cleaned_data['confirm_pass']
        val_name = cleaned_data['name']

        if val_conf_pass != val_pass:
            raise forms.ValidationError("Password Didn't Match")
        if len(val_name) < 15:
            raise forms.ValidationError("Name Must be at least 15 chars")
    