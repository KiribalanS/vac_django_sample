from  django.urls import path
from . import views

urlpatterns = [
    path('', views.home ),
    path('s/', views.shop),
    path('college/', views.college),
    path('html/', views.html),
    path('text', views.text),
    path('form', views.form),
    # path('submit', views.form),
    path('para/<str:name>', views.para ),

]
