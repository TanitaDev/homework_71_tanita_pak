from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views import *

router = routers.DefaultRouter()
router.register('posts', PostViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token, name='api_token_auth'),
    path('posts/', PostListView.as_view(), name='products_api'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='detail_products_api')
]
