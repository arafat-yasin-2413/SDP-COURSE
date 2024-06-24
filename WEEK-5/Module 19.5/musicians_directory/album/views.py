from django.shortcuts import render,redirect
from .forms import AlbumForm
from django.contrib import messages
from album.models import Album

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
# Create your views here.

# Add Album Funtion Based view
def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Album Added Successfully')
            return redirect('homepage')
    else:
        form = AlbumForm()
    return render(request,'add_album.html',{'form':form})

# Add Album Class Based View
class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self,form):
        response = super().form_valid(form)
        messages.success(self.request, 'Album Added by Class Based View Successfully')
        return response
    

# Edit Album Function Based View
def edit_album(request,id):
    single_album = Album.objects.get(pk=id)
    album_edit_form = AlbumForm(instance=single_album)
    if request.method == 'POST':
        album_edit_form = AlbumForm(request.POST, instance=single_album)
        if album_edit_form.is_valid():
            album_edit_form.save()
            return redirect('homepage')
    return render(request,'edit_album.html',{'form':album_edit_form})
    

# Edit Album Class Based View
class EditAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'edit_album.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self,form):
        response = super().form_valid(form)
        messages.success(self.request, 'Album Edited by Class Based View Successfully')
        return response
    

# Delete Album Function Based View
def delete_album(request,id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('homepage')

# Delete Album Class based view
class DeleteAlbumView(DeleteView):
    model = Album
    template_name = 'album_confirm_delete.html'
    success_url = reverse_lazy('homepage')

    def delete(self,request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Album deleted by Class Based View Successfully')
        return response