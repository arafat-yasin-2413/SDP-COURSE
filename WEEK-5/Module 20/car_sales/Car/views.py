from django.shortcuts import render,redirect
from django.contrib import messages

from .forms import CarForm,CommentForm
from .models import CarModel,Order

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarForm()
    return render(request,'add_car.html',{'form':form})


# @login_required
def car_details(request,id):
    single_car = CarModel.objects.get(pk=id)
    comments = single_car.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = single_car
            new_comment.save()
            return redirect('car_details', id=single_car.id)
    else:
        comment_form = CommentForm()
    return render(request,'car_details.html',{
        'car':single_car, 
        'comments':comments, 
        'comment_form': comment_form
        })


@login_required
def buy_now(request, id):
    car = CarModel.objects.get(pk=id)
    try:
        car.reduce_quantity()
        Order.objects.create(user=request.user, car = car, quantity=1)
        messages.success(request,'Purchase Successfull')
    except ValueError:
        messages.error(request,'Sorry, This car is Out of Stock.')
    return redirect('car_details', id = id)
