from django.shortcuts import render,redirect
from task.models import Task
from task.forms import TaskForm
# Create your views here.

def add_task(request):
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            status = task_form.cleaned_data['is_completed']
            # print(status)
            task_form.save()
            return redirect('show_task')
    else:
        task_form = TaskForm()    
    return render(request, 'add_task.html',{'form':task_form})
    

def edit_task(request,id):
    task = Task.objects.get(pk=id)
    task_form = TaskForm(instance=task)
    # print(task_form.taskTitle)

    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
    return render(request, 'add_task.html',{'form':task_form})



def delete_task(request,id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('show_task')