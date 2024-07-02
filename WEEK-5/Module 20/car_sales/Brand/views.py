from django.shortcuts import render, redirect
from .forms import BrandForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BrandForm()
    return render(request,'add_brand.html',{'form':form})

