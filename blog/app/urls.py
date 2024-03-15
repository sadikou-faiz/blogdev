from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.homepage , name=""),
    path('signup/' , views.signup , name="signup"),
    path('my_login/' , views.my_login , name="my_login"),
    path('logout/' , views.logout , name="logout"),
    path('dashboard/' , views.dashboard , name="dashboard"),
]  
 