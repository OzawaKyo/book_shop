from django.urls import path
from .views import *
from .views import BookList
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    path('',home,name='home'),
    path('add', addBook, name='add'),
    path('show',showBook, name='show'),
    path('books/', BookList.as_view()),
    path('books/<int:pk>', BookDetail.as_view(), name='book-detail'),
    path('users/', UserListView.as_view(),name='users'),
    path('get-token',obtain_auth_token)
]
