from django.urls import path
from .import views
urlpatterns = [
    # path('signup/',views.registration,name="signup"),
    path('signup/',views.RegistrationView.as_view(),name="signup"),
    # path('login/',views.user_login,name="login"),
    path('login/',views.UserLoginView.as_view(),name="login"),
    # path('logout/',views.user_logout,name="logout"),
    path('logout/',views.UserLogoutView.as_view(),name="logout"),
    
    path('profile/',views.user_profile,name="profile"),
    path('edit_profile/',views.edit_profile,name="edit_profile"),
    path('pass_change/',views.pass_change,name="pass_change"),

    
]
