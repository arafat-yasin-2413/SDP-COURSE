from django.urls import path
from .import views

urlpatterns = [
    path('signup/',views.signup, name="signup"),
    path('login/',views.user_login, name="login"),
    path('logout/',views.user_logout, name="logout"),
    path('profile/',views.user_profile, name="profile"),

    path('pass_change1/',views.pass_change1,name="pass_change1"),
    path('pass_change2/',views.pass_change2,name="pass_change2"),
    path('change_user_data/',views.change_user_data,name="change_user_data"),
    
    
]
