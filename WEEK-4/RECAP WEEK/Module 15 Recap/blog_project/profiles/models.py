from django.db import models
from author.models import Author
# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    author = models.OneToOneField(Author,on_delete=models.CASCADE,default=None)
    # ekjon author er ektai profile thakbe. (one to one)

    def __str__(self):
        return self.name
    
    
