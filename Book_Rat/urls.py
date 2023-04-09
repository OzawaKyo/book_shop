from django.urls import path
from .views import *
from .views import BookList
urlpatterns = [
    path('',home,name='home'),
    path('add', addBook, name='add'),
    path('show',showBook, name='show'),
    path('books/', BookList.as_view()),
]
