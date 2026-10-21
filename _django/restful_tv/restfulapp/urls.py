from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('shows/<int:id>/', views.the_show),
    path('show/<int:id>/destroy/', views.destroy),
    path('shows/<int:id>/update/', views.update),
]