
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('base/',views.base, name="base"),
    path('',include('first_app.urls')),

]
