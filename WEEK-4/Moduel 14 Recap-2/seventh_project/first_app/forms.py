from django import forms 
from first_app.models import StudentModel


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # exclude = ['roll']

        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll',

        }
