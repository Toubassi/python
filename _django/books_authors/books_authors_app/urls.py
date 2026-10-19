from django.urls import path
from . import views

urlpatterns =[
  path('', views.index),
  path('add-book/', views.add_book),
  path('add-author/', views.add_author),
  path('books/<int:id>/', views.book_details),
  path('authors/<int:id>/', views.author_details),
  path('authors/<int:id>/add-book/', views.add_book_to_author),
  path('books/<int:id>/add-author/', views.add_author_to_book),
]