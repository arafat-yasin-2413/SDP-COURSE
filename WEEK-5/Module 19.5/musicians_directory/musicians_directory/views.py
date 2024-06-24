from django.shortcuts import render,redirect
from album.models import Album
from musician.models import Musician

def home(request):
    all_allbum = Album.objects.all()
    return render(request,'home.html',{'data':all_allbum})

def base(request):
    return render(request,'base.html')