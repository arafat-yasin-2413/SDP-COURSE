from django import forms 

from task.models import Task 

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        is_completed = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'custom-checkbox-class'}))

        widgets = {
            'assignDate':forms.DateTimeInput(attrs={'type':'datetime-local'}),

        }