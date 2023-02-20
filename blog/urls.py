
from django.contrib import admin
from django.urls import path, include
from .views import *



urlpatterns = [
    path('signup/', signupfunc, name = 'signup'),
    path('login/', loginfunc, name = 'login'),
    path('logout/', logoutfunc, name = 'logout'),
    path('list/', listfunc, name ='list'),
    path('detail/<int:pk>', detailfunc, name ='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name ='read'),
] 
