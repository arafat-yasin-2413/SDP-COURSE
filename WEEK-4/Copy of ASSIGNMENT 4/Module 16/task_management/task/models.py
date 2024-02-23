from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    assignDate = models.DateTimeField()
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return f"{self.taskTitle}"