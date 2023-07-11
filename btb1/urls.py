from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   
    path('',views.loginpage,name='loginpage'),
    path('homepage',views.homepage,name='homepage'),
    path('signuppage',views.signuppage,name='signuppage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('prd',views.prd,name='prd'),#post related details
    path('give_flat',views.give_flat,name='give_flat')

  
   



    
]
