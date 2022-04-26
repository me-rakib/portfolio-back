from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%b %d, %Y, %H:%M %p")
    class Meta:
        model = BlogPost
        fields = ('id' ,'title', 'text', 'date')