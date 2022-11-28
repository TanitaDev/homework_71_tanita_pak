from django import forms

from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']
        exclude = ['author']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти пользователя")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'comment-box', "placeholder": "Добавить комментарий"})}
