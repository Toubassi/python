from django.urls import path, include
from . import views

urlpatterns =[
  path('', views.root),
  path('blogs/', views.index),
  path('blogs/create/', views.create),
  path('blogs/<number>/', views.number),
  path('blogs/<number>/edit', views.edit),
  path('blogs/<number>/destroy', views.destroy),
]