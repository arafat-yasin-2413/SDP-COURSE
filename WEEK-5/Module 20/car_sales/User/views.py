from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.edit import FormView 
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy


from django.shortcuts import render,redirect
from .forms import RegistrationForm,EditUserDataForm
from Car.models import Order

from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required



# Create your views here.

# registration function based view
def registration(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,'Account Created Successfully')
            return redirect('signup')
    else:
        register_form = RegistrationForm()
    return render(request,'register.html',{'form':register_form})

# registration class based view
class RegistrationView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        form.save()
        messages.success(self.request, 'Account Created Successfully')
        return super().form_valid(form)
    


# user login function based view
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request,data = request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_pass =  form.cleaned_data['password']
                user = authenticate(username = user_name, password = user_pass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Login Successfull')
                    return redirect('login')
                else:
                    messages.warning(request,'Login Information Incorrect')
                    return redirect('login')
        else:
            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return redirect('profile')


# user login class based view
class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    
    def dispatch(self, request, *args,**kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request,'Login Successfull')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Login Information Incorrect.')
        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('profile')
        
    
    

# user logout function based view
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logout Successfull')
        return redirect('home')
    else:
        return redirect('login')


# user logout class based view
class UserLogoutView(LogoutView):
    def get(self,request):
        if request.user.is_authenticated:
            logout(request)
            messages.success(request, 'Logout Successfull')
        return redirect('login')

@login_required
def user_profile(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user = request.user)
        return render(request,'profile.html',{
            'user':request.user,
            'orders':orders
            })
    else:
        return redirect('login')
    
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditUserDataForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Updated Successfully')
            return redirect('profile')
    else:
        form = EditUserDataForm(instance=request.user)
    return render(request,'edit_profile.html',{'form':form})


@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request,'Password Changed Successfully')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'pass_change.html',{'form':form})
