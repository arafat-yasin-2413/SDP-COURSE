from django.shortcuts import render
from posts.models import Post
from django.contrib.auth.models import User
from categories.models import Category


def home(request,category_slug=None):
    data = Post.objects.all()
    if category_slug is not None:
        category_name = Category.objects.get(slug=category_slug)
        data = Post.objects.filter(category=category_name)
    categories = Category.objects.all()
    return render(request,'home.html',{'data':data, 'category':categories})


def all_author(request):
    authors = User.objects.all()
    print(authors)
    return render(request,'all_author.html',{'data':authors})
