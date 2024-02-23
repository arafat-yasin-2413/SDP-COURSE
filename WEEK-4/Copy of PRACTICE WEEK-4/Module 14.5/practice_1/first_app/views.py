from django.shortcuts import render
from first_app.forms import StudentForm, MyForm, NewForm
# Create your views here.

def home(request):
    if request.method == "POST":
        form = NewForm(request.POST,request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('first_app/uploads/' + 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = NewForm()
    return render(request, 'home.html',{'form':form})
