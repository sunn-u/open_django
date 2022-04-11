# Coding by SunWoo(tjsntjsn20@gmail.com)

from django.contrib import admin
from django.urls import path, include
from FirstApp import views


urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read),
    path('delete/', views.delete),
    path('update/<id>/', views.update)
]
