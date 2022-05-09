from django import urls
from django.urls import path
from .views import GetBooks, AddBook, BookDetails
urlpatterns = [
    path('', GetBooks.as_view()),
    path('add/', AddBook.as_view()),
    path('<int:pk>', BookDetails.as_view()),
]
