from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('main',main,name='main'),
    path('detail/<str:car_name>',detail,name='detail'),
    path('register',register,name='register'),
    path('user',user,name='user'),
    path('passwordChange',passwordChange,name='passwordChange'),
    path('home',home,name="home"),
]