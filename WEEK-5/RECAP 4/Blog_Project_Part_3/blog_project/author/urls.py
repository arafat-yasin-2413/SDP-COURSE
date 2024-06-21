from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    # path('login/', views.user_login, name="login"),
    path('login/', views.UserLoginView.as_view(), name="login"),
    # path('logout/', views.user_logout, name="logout"),
    path('logout/', views.LogoutView.as_view(), name="logout"),

    path('profile/', views.profile, name="profile"),
    path('edit_profile/',views.edit_profile,name="edit_profile"),
    path('pass_change/',views.pass_change,name="pass_change"),
    

    path('show_post_in_profile/', views.show_post_in_profile, name="show_post_in_profile"),
    

    

]

