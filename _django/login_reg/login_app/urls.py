from django.urls import path
from . import views

urlpatterns = [
    path('', views.register),
    path('success/', views.success),
    path('home/', views.home),
    path('logout/', views.logout)
]
