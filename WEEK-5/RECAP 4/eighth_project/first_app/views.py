from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import update_session_auth_hash

from .forms import ChangeUserDataForm

# Create your views here.
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request,'Account Created Successfully')
                form.save()
        else:
            form = RegisterForm()
        return render(request,'signup.html',{'form':form})
    else:
        return redirect('profile')

    

def user_login(request):
    if not request.user.is_authenticated:
        if(request.method == 'POST'):
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username= name, password = user_pass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login Successfull')
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('profile')
    


def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'user':request.user})
    else:
        return redirect('login')
    
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logout Successfull')
        return redirect('home')
    else:
        return redirect('login')
    

def pass_change1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user,request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, request.user)
                messages.success(request,'Password with old password Changed Successfully')
                return redirect('profile')
        else:
            form = PasswordChangeForm(request.user)
        return render(request,'pass_change1.html',{'form':form})
    else:
        return redirect ('login')


def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(request.user,request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, request.user)
                messages.success(request,'Password without old password Changed Successfully')
                return redirect('profile')
        else:
            form = SetPasswordForm(request.user)
        return render(request,'pass_change2.html',{'form':form})
    else:
        return redirect ('login')


def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserDataForm(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request,'User Data Changed Successfully')
                return redirect('home')
        else:
            form = ChangeUserDataForm(instance = request.user)
        return render(request,'change_user_data.html',{'form':form})
    else:
        return redirect('profile')
