from django.http import HttpResponse
from django.shortcuts import render, redirect
from posts.models import Post
from .forms import RegistrationForm
from .forms import ChangeUserDataForm
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import update_session_auth_hash


from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator






# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Registration Successfull')
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request,data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username = user_name, password = user_pass)
                if user is not None:
                    messages.success(request,'Login Successfull')
                    login(request,user)
                    return redirect('profile')
                else:
                    messages.warning(request,'Login Information Incorrect')
                    return redirect('login')
        else:   
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form}) 
    else:
        return redirect('profile')


class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request,'Login by CBV Successfull')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Login Info Inceorrect by CBV')
        return super().form_invalid(form)
    



def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('login')
    

# def profile(request):
#     if request.user.is_authenticated:
#         return render(request,'profile.html',{'user':request.user})
#     else:
#         return redirect('login')

@login_required
def profile(request):
    return render(request,'profile.html',{'user':request.user})
        
    
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ChangeUserDataForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('profile')
    else:
        form = ChangeUserDataForm(instance =request.user)
    return render(request,'edit_profile.html',{'form' : form})


def pass_change(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,request.user)
            messages.success(request,'Password Changed Successfully')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'pass_change.html',{'form':form})

@login_required
def show_post_in_profile(request):
    all_post_of_author = Post.objects.filter(author=request.user)
    print(all_post_of_author)
    return render(request,'profile.html',{'data':all_post_of_author})