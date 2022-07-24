from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from users.api.api_v1 import UserListRegisterAPIView, UserUpdateProfileAPIView

api_v1 = [
    path('users/', UserListRegisterAPIView.as_view(), name='user-list-create'),
    path('users/me/update', UserUpdateProfileAPIView.as_view()),
    path('users/login', obtain_auth_token, name='user-login'),
]

urlpatterns = [
    path('v1/', include(api_v1))
]
