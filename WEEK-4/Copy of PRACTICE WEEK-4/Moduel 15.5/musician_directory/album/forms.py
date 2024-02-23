from django import forms 
from album.models import Album 

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album 
        fields ="__all__"
        widgets = {
            'release_date':forms.DateInput(attrs={'type':'date'}),
            'rating':forms.NumberInput(attrs={'type':'number','min':1,'max':5,'step':1})
        }
        labels = {
            'rating':'Rate this album within 1 to 5',
            
        }
