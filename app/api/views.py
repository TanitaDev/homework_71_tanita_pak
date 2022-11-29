from profile import Profile

from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializer import PostSerializer
from posts.models import Post


class PostViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostListView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


class PostDetailView(APIView):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        data = {'product': PostSerializer(post).data}
        return Response(data, status=200)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        task = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(data=request.data)
        task.delete()
        if serializer.is_valid():
            task = serializer.save()
            return Response(data={"id": task.id})
        else:
            return Response(serializer.errors, status=404)


class LikeApi(APIView):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk='pk')
        account = get_object_or_404(Profile, pk='pk')
        if post and account:
            post.user_likes.add(account.pk)
            return Response(status=200)
        else:
            return Response(status=404)

    def delete(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk='pk')
        account = get_object_or_404(Profile, pk='pk')
        if post and account:
            post.user_likes.remove(account.pk)
            return Response(status=200)
        else:
            return Response(status=404)
