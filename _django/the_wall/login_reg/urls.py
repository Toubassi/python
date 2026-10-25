from django.urls import path
from . import views

urlpatterns = [
  path('', views.login),
  path('reg/', views.reg),
  path('logout/', views.logout)
]