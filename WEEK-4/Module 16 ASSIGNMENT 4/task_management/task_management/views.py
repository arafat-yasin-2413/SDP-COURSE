from django.shortcuts import render, redirect
from task.models import Task
from task.forms import TaskForm

def show_task(request):
    data = Task.objects.all()
    # print(data)
    # print(data.is_completed)
    return render(request, 'show_task.html',{'data':data})
