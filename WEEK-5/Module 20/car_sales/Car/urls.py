from django.urls import path
from .import views

urlpatterns = [
    path('add_car/',views.add_car, name="add_car"),
    path('car_details/<int:id>/',views.car_details, name="car_details"),
    path('buy_now/<int:id>/',views.buy_now, name="buy_now"),
    
    
    
]
