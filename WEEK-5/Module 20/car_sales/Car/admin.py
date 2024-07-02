from django.contrib import admin
from Car.models import CarModel,Comment, Order
# Register your models here.

admin.site.register(CarModel)
admin.site.register(Comment)
admin.site.register(Order)


