from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="User Name")
    file = forms.FileField()
    
    
    # email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # brithday = forms.DateField()
    # appointment = forms.DateTimeField()
    # CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    # size = forms.ChoiceField(choices=CHOICES)
    # MEAL = [('P','Pepperoni'),('M','Mushroom'),('B','Beef')]
    # pizza = forms.MultipleChoiceField(choices=MEAL)