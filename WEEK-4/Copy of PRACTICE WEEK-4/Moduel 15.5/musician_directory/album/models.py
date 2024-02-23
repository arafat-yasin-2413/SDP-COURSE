from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(Musician, on_delete =models.CASCADE)

    def __str__(self):
        return f"{self.album_name}"