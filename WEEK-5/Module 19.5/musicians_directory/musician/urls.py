from django.urls import path
from .import views
urlpatterns = [
    # path('register/',views.register_musician,name="register"),
    path('register/',views.CreateMusicianView.as_view(),name="register"),
    # path('login/',views.musician_login,name="login"),
    path('login/',views.MusicianLoginView.as_view(),name="login"),
    path('logout/',views.MusicianLogoutView.as_view(),name="logout"),
    path('profile/',views.ProfileView.as_view(),name="profile"),
    # path('edit_musician/<int:id>/',views.edit_musician,name="edit_musician"),
    path('edit_musician/<int:pk>/',views.EditMusicianView.as_view(),name="edit_musician"),

]
