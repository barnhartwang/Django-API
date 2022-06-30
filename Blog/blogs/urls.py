#blogs/urls.py
from django.urls import path
from blogs.views import BlogDetailAPIViewV1, BlogListAPIViewV1

urlpatterns = [
    path ('', BlogListAPIViewV1.as_view() ),
    path ('<int:pk>/', BlogDetailAPIViewV1.as_view()),
]
