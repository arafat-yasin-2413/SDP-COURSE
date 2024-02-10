from django.shortcuts import render



# Create your views here.
data = [
    {'id': 1, 'name': 'Moshiur'},
    {'id': 2, 'name': 'Nayeem'},
    {'id': 3, 'name': "Shakur"},
    {'id': 4, 'name': "Sohag"},

]

def home(request):
    return render(request, 'first_app/index.html',context={'list_of_dict':data})

def about(request,x):
    return render(request,'first_app/index.html',{'id':x})

def about2(request):
    print(request.GET)
    return render(request,'first_app/index.html',{'elements':request.GET})


# <a href="{% url 'about' x=id %}">About</a>


def base(request):
    return render(request,'first_app/base.html')

def home(request):
    return render(request,'first_app/home.html')