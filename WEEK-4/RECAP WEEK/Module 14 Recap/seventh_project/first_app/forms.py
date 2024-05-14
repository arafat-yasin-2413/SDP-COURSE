from django import forms 
from . models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # fields = ['name','roll',]
        labels = {
            'name':'Student Name',
            'roll':'Student Roll',
        }

        widgets = {
            # 'roll': forms.PasswordInput()
        }

        help_texts = {
            'name':'Write your full name'
        }

        error_messages = {
            'name':{'required':'Your name is required'}
        }