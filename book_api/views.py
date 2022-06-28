from django.shortcuts import render
from rest_framework import generics

from book_api.serializers import BookSerializer
from books.models import Book

class BookListAPIView(generics.ListAPIView):
    queryset =Book.objects.all()
    serializer_class = BookSerializer 
