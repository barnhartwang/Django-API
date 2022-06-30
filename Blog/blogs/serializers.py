from rest_framework import serializers
from blogs.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("id", "author", "title", "body", "created_at", "updated_at")

