from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from posts.forms import PostForm
from posts.models import Post


class AddPost(LoginRequiredMixin, CreateView):
    template_name = 'add_post.html'
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


class UpdatePost(UpdateView):
    template_name = 'update_post.html'
    model = Post
    form_class = PostForm

    # def test_func(self):
    #     return self.get_object().author == self.request.user or self.request.user.has_perm('core.change_post')

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})


class DeletePost(DeleteView):
    template_name = 'delete_post.html'
    model = Post
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})
