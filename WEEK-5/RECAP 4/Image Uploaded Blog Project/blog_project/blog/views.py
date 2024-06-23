from django.shortcuts import render,redirect
from . forms import BlogForm
from . models import Blog

# Create your views here.

def create_blogs(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request,'create_blog.html',{'form':form})


def blog_list(request):
    all_blog = Blog.objects.all()
    return render(request,'blog_list.html',{'data':all_blog})




