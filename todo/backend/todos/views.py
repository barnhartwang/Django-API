#todos/views.py
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from todos.models import Todo
from todos.serializers import TodoSerializer

class TodoListAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetialAPIView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    
