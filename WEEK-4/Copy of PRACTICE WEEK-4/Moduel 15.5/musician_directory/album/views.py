from django.shortcuts import render,redirect
from album.forms import AlbumForm
from album.models import Album

# Create your views here.
def add_album(request):
    if request.method == "POST":
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form= AlbumForm()
    return render(request, 'add_album.html',{'form':album_form})
 
def edit_album(request,id):
    album = Album.objects.get(pk=id)
    album_form = AlbumForm(instance=album)
    # print(album.album_name)

    if request.method == "POST":
        album_form = AlbumForm(request.POST,instance=album )
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    return render(request, 'add_album.html',{'form':album_form})


def delete_album(request,id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('homepage')
