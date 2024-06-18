from django.shortcuts import render,redirect
from . import forms 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.



def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.RegistrationForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account Created Successfully')
                form.save()
                # print(form.cleaned_data)
        else:
            form = forms.RegistrationForm()
        return render(request,'signup.html',{'form':form})
    else:
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'user':request.user})
    else:
        return redirect('login')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=name,password = userpass)
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('profile')


def user_logout(request):
    logout(request)
    return redirect('login')



def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request,user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'pass_change.html',{'form':form})
    else:
        return redirect('login')

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request,user)
                return redirect('profile')
        else:
            form = SetPasswordForm(request.user)
        return render(request, 'pass_change2.html',{'form':form})
    else:
        return redirect('login')
    

def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request,'User Data Has Changed Successfully')
                form.save()
        else:
            form = forms.ChangeUserData(instance=request.user)
        return render(request,'change_data.html',{'form':form})
    else:
        return redirect('signup')
