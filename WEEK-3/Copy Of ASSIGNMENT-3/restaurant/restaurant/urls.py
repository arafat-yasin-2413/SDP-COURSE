
from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.base),
    path('',views.myRest, name="myRest"),
    path('home/',views.home, name="home"),

    path('meal/',include('meal.urls')),
    path('about-us/',include('about_us.urls')),
]
