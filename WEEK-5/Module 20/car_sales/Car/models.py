from django.db import models
from Brand.models import BrandModel
from django.contrib.auth.models import User 

# Create your models here.
class CarModel(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='car_images/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.title
    
    def reduce_quantity(self, amount=1):
        if self.quantity >= amount:
            self.quantity -= amount
            self.save()
        else:
            raise ValueError("Not Enough Quantity Available")
    


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='orders')
    created_on = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
    





class Comment(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comment by {self.name}"
    