from django.urls import path 
from diabetico import views

urlpatterns = [
    path('', views.mysite, name='mysite'), 
]