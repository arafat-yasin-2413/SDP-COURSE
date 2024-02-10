from django.urls import path

from . import views
urlpatterns = [
    path('menu/',views.menu, name= "menu"),
    path('show-item/',views.show_item, name="show-item"),
    path('index/',views.index,name="foods"),
]
