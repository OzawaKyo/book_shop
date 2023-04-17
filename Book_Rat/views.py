from django.shortcuts import render
from .models import Book
from .forms import BookForm
from django.http import HttpResponse
from .serializers import BookSerializer
from rest_framework import generics , authentication , permissions
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.contrib.auth.models import User 



def addBook(request):
    form = BookForm()
    if request.method == 'POST':
        print('Printing Post :', request.POST)
        form = BookForm(request.POST)
        form.save()
    context = {'form' : form}
    return render(request, './addBook.html', context)
 
def showBook(request):
    books = Book.objects.all()
    return render(request, './showBook.html',{'books':books})


def home(request):
    return render(request,'./home.html',{"titre":"hamid"})


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer    

class UserListView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self , request , format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)