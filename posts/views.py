from rest_framework import generics, permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


# Create your views here.

# ListAPIView only display a list of data
# class PostList(generics.ListAPIView):

# ListCreateAPIView display a list and the ability to create a post
# class PostList(generics.ListAPIView):

class PostList(generics.ListCreateAPIView):
    # 1- what we are hopping to display
    queryset = Post.objects.all()
    # 2 -what serializer we are going to use
    serializer_class = PostSerializer
    # we specify who has the permission to call this API:
    # permission_classes = [permissions.IsAuthenticated]
    # if not authenticated just have only right to read
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # before saving something into the database
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class PostRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_class = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        post = Post.objects.filter(poster=self.request.user,pk=self.kwargs['pk'])
        if post.exists():
            self.destroy(request, *args, **kwargs)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You can not delete this post, it does not exist anymore')
