
from django.contrib import admin
from django.urls import path,include
from .import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base/',views.base,name="base"),
    path('',views.home, name="home"),

    #includes apps urls 
    path('',include('User.urls') ),
    path('',include('Car.urls') ),
    path('',include('Brand.urls') ),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
