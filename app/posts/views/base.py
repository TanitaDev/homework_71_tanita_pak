from django.views.generic import ListView

from posts.forms import CommentForm
from posts.models import Post, Comment


class IndexView(ListView):
    template_name = "index.html"
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['comment_form'] = CommentForm()
        context['posts'] = Post.objects.order_by('-created_at')
        context['comments'] = Comment.objects.order_by('-created_at')
        return context
