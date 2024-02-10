from django.shortcuts import render



def base(request):
    return render(request,'base.html')

def myRest(request):
    return render(request,'myRest.html')

def home(request):
    return render(request,'home.html')


