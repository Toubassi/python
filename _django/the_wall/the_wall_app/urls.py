from django.urls import path
from . import views

urlpatterns = [
  path('', views.wall),
  path('post/', views.post, name='post'),
  path('comment/<int:id>/', views.comment, name='comment'),
  path('edit/<int:id>/', views.edit, name='edit'),
  path('delete/<int:id>/', views.delete, name='delete')
  
]