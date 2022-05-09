from django import urls
from django.urls import path
from .views import getBooks, addBook, book
urlpatterns = [
    path('', getBooks),
    path('<int:pk>', book),
    path('add/', addBook),
]
