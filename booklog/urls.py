from django.urls import path, include
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('add/', views.add_book, name='add_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),

]

