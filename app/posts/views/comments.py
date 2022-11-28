from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import FormView

from accounts.models import Account
from posts.forms import CommentForm
from posts.models import Comment, Post


class CommentView(LoginRequiredMixin, FormView):
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            user = request.user
            Comment.objects.create(author=user, post=post, text=text)
        return redirect('index')
