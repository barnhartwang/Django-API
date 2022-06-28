#book_api/urls.py
from django.urls import path

from book_api import views

urlpatterns = [
    path('',views.BookListAPIView.as_view() )
]
