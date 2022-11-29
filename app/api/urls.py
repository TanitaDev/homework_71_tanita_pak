from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views import *

router = routers.DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', PostListView.as_view(), name='products_api'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='detail_products_api'),
    path('likes/', LikeApi.as_view(), name='like_api'),
    path('login/', obtain_auth_token, name='api_token_auth')
]
