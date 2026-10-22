from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('confirm/<int:id>/', views.confirm),
    path('destroy/<int:id>/', views.destroy)
]