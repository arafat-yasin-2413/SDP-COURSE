from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Musician(AbstractUser):
    phone_number = models.CharField(max_length=12)
    instrument_type = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
