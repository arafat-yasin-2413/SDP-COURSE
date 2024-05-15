from django.shortcuts import render,redirect
from . forms import PostForm
from . import models
# Create your views here.

def add_post(request):
    if request.method=='POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
    else:
        post_form = PostForm()
    return render(request,'add_post.html',{'form':post_form})


def edit_post(request,id):
    single_post = models.Post.objects.get(pk=id)
    post_form = PostForm(instance=single_post)
    if request.method == 'POST':
        post_form = PostForm(request.POST,instance=single_post)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
    
    return render(request,'add_post.html',{'form':post_form})


def delete_post(request,id):
    single_post = models.Post.objects.get(pk=id)
    single_post.delete()
    return redirect("home")