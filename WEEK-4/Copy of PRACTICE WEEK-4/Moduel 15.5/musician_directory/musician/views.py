from django.shortcuts import render,redirect
from musician.forms import MusicianForm
from musician.models import Musician

# Create your views here.
def add_musician(request):
    if request.method == "POST":
        musician_form = MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    else:
        musician_form= MusicianForm()
    return render(request, 'add_musician.html',{'form':musician_form})


def edit_musician(request,id):
    musician = Musician.objects.get(pk=id)
    musician_form = MusicianForm(instance=musician)
    # print(musician)

    if request.method == "POST":
        musician_form = MusicianForm(request.POST,instance=musician )
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    return render(request, 'add_musician.html',{'form':musician_form})
