from django.urls import path

from posts.views.base import IndexView
from posts.views.comments import CommentView
from posts.views.post_like import LikePost
from posts.views.search import SearchView
from posts.views.posts import AddPost
from posts.views.subscribe import SubscribeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-post', AddPost.as_view(), name='add_post'),
    path('search', SearchView.as_view(), name='search'),
    path('like/<int:pk>', LikePost.as_view(), name='like'),
    path('subscribe/<int:pk>', SubscribeView.as_view(), name='subscribe'),
    path('comment/<int:pk>', CommentView.as_view(), name='comment')
]
