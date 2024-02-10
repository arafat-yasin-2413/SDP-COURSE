from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('about/page/<int:x>/',views.about, name="about"),
    path('about2/',views.about2, name="about2"),


    path('base/',views.base),
    path('home/',views.home),
    
]
