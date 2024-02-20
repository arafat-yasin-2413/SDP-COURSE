from django.db import models

# Create your models here.
class StudentModel(models.Model):
    roll = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=40)
    father_name = models.CharField(max_length=40)
    address = models.TextField()


    def __str__(self):
        return f"{self.name} - Roll {self.roll}"
    