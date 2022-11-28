from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView

from posts.forms import PostForm
from posts.models import Post


class LikePost(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        if request.user in post.user_likes.all():
            post.user_likes.remove(request.user)
            return redirect('index')
        post.user_likes.add(request.user)
        return redirect('index')
