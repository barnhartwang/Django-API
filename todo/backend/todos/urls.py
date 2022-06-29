#Todos/urls.py
from django.urls import path

from todos.views import TodoDetialAPIView, TodoListAPIView
urlpatterns = [
    path ('', TodoListAPIView.as_view()),
    path ('<int:pk>/', TodoDetialAPIView.as_view())
]
