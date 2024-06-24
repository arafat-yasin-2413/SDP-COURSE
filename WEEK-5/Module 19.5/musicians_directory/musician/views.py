from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from . models import Musician
from . forms import MusicianForm, ChangeMusicianDataForm
from django.contrib import messages


from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import UpdateView

# Create your views here.
# Create Musician with Function Based View
def register_musician(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = MusicianForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Registered Successfully')
                return redirect('homepage')
            else:
                messages.warning(request,'Registration failed. Provide Correct Info.')
        else:
            form = MusicianForm()
        return render(request,'register.html',{'form':form})
    else:
        return redirect('login')




# Create Musician Class Based View
class CreateMusicianView(LoginRequiredMixin, CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'register.html'
    success_url = reverse_lazy('homepage')
    login_url = 'login'

    def form_valid(self,form):
        response = super().form_valid(form)
        messages.success(self.request, 'Created Musician By Class Based View Successfully')
        return response
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.warning(self.request, 'Registration Failed by Class Based View. Provide Correct Info.')
        return response
    

    






# Musician Login Function Based View
def musician_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password = user_pass)
            if user is not None:
                messages.success(request,'Login Successfull')
                login(request,user)
                return redirect('homepage')
            else:
                messages.warning(request,'Login Information Incorrect')
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

# Musician Login Class Based View
class MusicianLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Login by Class Based View Successfull')    
        return super().form_valid(form)
    
    
# Musician Logout Class Based View
class MusicianLogoutView(LogoutView):
    next_page = reverse_lazy('homepage')

    def dispatch(self, request, *args, **kwargs):
        messages.info(self.request, 'Log out by Class Based View Successfull')
        return super().dispatch(request, *args, **kwargs)


# Musician Profile by Class Based View
class ProfileView(TemplateView):
    template_name = 'profile.html'


# Edit Musician Function Based View
def edit_musician(request,id):
    musician = Musician.objects.get(pk=id)
    edit_form = ChangeMusicianDataForm(instance= musician)
    if request.method == 'POST':
        edit_form = ChangeMusicianDataForm(request.POST, instance=musician)
        if edit_form.is_valid():
            messages.success(request,'Musician Edited by Function Based View Successfully')
            edit_form.save()
            return redirect('homepage')
    return render(request,'edit_musician.html',{'form':edit_form})


        
# Edit Musician Class Based View
class EditMusicianView(LoginRequiredMixin, UpdateView):
    model = Musician
    form_class = ChangeMusicianDataForm
    template_name = 'edit_musician.html'
    success_url = reverse_lazy('homepage')
    login_url = 'login'

    def form_valid(self,form):
        messages.success(self.request, 'Musician Edited by Class Based View Successfully')
        return super().form_valid(form)
    
    