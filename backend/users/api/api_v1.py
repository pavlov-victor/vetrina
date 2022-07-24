from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, UpdateAPIView

from users.serializers import UserRegisterSerializer, UserUpdateProfileSerializer

User = get_user_model()


class UserListRegisterAPIView(ListCreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return User.objects.filter(is_active=True, hide=False)


class UserUpdateProfileAPIView(UpdateAPIView):
    serializer_class = UserUpdateProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
