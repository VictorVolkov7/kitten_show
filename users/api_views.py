from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView as BaseTokenObtainPairView,
    TokenRefreshView as BaseTokenRefreshView,
)

from users.models import User
from users.serializers import UserCreateSerializer


@extend_schema(summary="Create a new user controller.")
class UserCreateAPIView(CreateAPIView):
    """
    Endpoint for creating a new User.
    """

    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        password = serializer.validated_data.pop("password", None)
        instance = User.objects.create(**serializer.validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save(update_fields=["password"])
        return serializer.instance


@extend_schema(
    summary="Used to request a pair of tokens.",
)
class TokenObtainPairView(BaseTokenObtainPairView):
    """
    A placeholder for a class to supplement documentation.
    """

    pass


@extend_schema(
    summary="Access token updates.",
)
class TokenRefreshView(BaseTokenRefreshView):
    """
    A placeholder for a class to supplement documentation.
    """

    pass
