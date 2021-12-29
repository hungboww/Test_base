from django.conf import settings
from django.conf.urls import url
from django.urls import path

from apps.users.views import UserListCreateAPIView, UserDetailUpdateAPIView

urlpatterns = [
    url(r'^/users$', UserListCreateAPIView.as_view(), name='user_list'),
    path('/user/<int:pk>', UserDetailUpdateAPIView.as_view(), name='user_detail_update'),
]
