from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.serializers import UserSerializer


class UserCreateApiView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

