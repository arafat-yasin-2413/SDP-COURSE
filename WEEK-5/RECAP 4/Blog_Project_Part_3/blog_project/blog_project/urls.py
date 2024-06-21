
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="homepage"),
    path('author/',include('author.urls')),
    path('post/',include('posts.urls')),
    path('category/',include('categories.urls')),
    path('all_author/',views.all_author, name="all_author"),
    path('category/<slug:category_slug>/',views.home, name="category_wise_post"),
    

]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
