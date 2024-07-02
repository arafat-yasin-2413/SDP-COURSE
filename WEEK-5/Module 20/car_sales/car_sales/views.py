from django.shortcuts import render,redirect
from Car.models import CarModel
from Brand.models import BrandModel

def base(request):
    return render(request,'base.html')

def home(request):
    brands= BrandModel.objects.all()
    cars = CarModel.objects.all()
    selected_brand = request.GET.get('brand')

    if selected_brand:
        cars = cars.filter(brand_id = selected_brand)
    context = {
        'brands':brands,
        'cars':cars,
        'selected_brand':selected_brand
    }

    return render(request,'home.html',context)