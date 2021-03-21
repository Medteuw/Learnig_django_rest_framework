from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


# Create your views here.

class PostList(generics.ListAPIView):
    # 1- what we are hopping to display
    queryset = Post.objects.all()
    # 2 -what serializer we are going to use
    serializer_class = PostSerializer
