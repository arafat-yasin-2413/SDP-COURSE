from django.shortcuts import render, redirect
from posts.forms import PostForm
from posts.models import Post

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author=request.user
            post_form.save()
            return redirect('homepage')
    else:
        post_form = PostForm()
    return render(request, 'add_post.html',{'form':post_form}) 


def edit_post(request,id):
    post = Post.objects.get(pk=id)
    post_form = PostForm(instance=post)
    # print(post.title)

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.instance.author=request.user
            post_form.save()
            return redirect('homepage')
    return render(request, 'edit_post.html',{'form':post_form}) 


def delete_post(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')