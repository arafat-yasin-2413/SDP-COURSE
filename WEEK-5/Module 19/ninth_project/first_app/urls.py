from django.urls import path
from .import views

urlpatterns = [
    # path('',views.home, name="home"),
    path('',views.set_session),
    # path('get/',views.get_cookie, name="get_cookie"),
    path('get/',views.get_session),
    # path('delete/',views.delete_cookie, name="delete_cookie"),
    path('delete/',views.delete_session),

]
