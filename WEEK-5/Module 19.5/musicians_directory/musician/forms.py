from django import forms 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from musician.models import Musician

class MusicianForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'required'}))
    class Meta(UserCreationForm.Meta):
        model = Musician
        fields = ['username','first_name','last_name','email','phone_number','instrument_type']

class ChangeMusicianDataForm(UserChangeForm):
    password = None
    class Meta:
        model = Musician
        fields = ['username','first_name','last_name','email','phone_number','instrument_type']