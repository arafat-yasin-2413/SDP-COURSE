from django.shortcuts import render,redirect
from django.contrib.auth.models import User

def base(request):
    return render(request,'base.html')

def home(request):
    data = User.objects.all()
    return render(request, 'home.html',{'data':data})