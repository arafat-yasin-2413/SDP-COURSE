from django.shortcuts import render,redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView,LogoutView
from .forms import UserRegistrationForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy

from .forms import UserRegistrationForm,UserUpdateForm
from django.views import View
# Create your views here.


class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        print(form.cleaned_data)
        user = form.save()
        """
        forms.py er save method ekta 'our_user' return kortese. sei our_user ta ke
        amra eikhane 'user' er moddhe receive kortesi
        """

        """
        ekhon amra user pawar por orthat, form er kaj jodi thikmoto thake, tahole 
        amra ekhon user k login koraya dibo
        """
        login(self.request,user)
        print(user)
        return super().form_valid(form) 
        # form_valid method ta jeno automatically call hoy seijonno 
        # amra return super().form_valid(form) likhechi. jar maddhome nijekei call kortese 
        # ebong sei sathe form ta keu pass kore dicche. 
        # jodi sobkichu thik thake tahole form_valid method ta call hobe
    

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')
    

class UserBankAccountUpdateView(View):
    template_name='accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form':form})
    
    def post(self,request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request,self.template_name, {'form':form})
    