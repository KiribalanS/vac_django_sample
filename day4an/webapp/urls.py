from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('aakash',views.shop),
    path('nv/<str:name>',views.aakash),
    path('loop', views.loop)
]