from django.shortcuts import render
from .serializers import BlogPostSerializer 
from rest_framework import viewsets      
from .models import BlogPost                 

class BlogPostView(viewsets.ModelViewSet):  
    serializer_class = BlogPostSerializer   
    queryset = BlogPost.objects.all()     
    http_method_names = ['get','head']