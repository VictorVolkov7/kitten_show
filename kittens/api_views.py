from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import status, serializers
from rest_framework.generics import (
    ListAPIView,
    DestroyAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    CreateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from kittens.filter import BreedFilter
from kittens.models import Kitten
from kittens.permissions import IsOwner
from kittens.serializers import (
    KittenListRetrieveSerializer,
    KittenCreateUpdateSerializer,
)


@extend_schema(summary="Viewing the list of kittens.")
class KittenListApiView(ListAPIView):
    """Endpoint for viewing the list of kittens."""

    queryset = Kitten.objects.select_related("breed", "owner").all()
    serializer_class = KittenListRetrieveSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BreedFilter
    permission_classes = [IsAuthenticated]


@extend_schema(summary="Getting information about a kitten.")
class KittenRetrieveAPIView(RetrieveAPIView):
    """Endpoint for viewing the kitten."""

    queryset = Kitten.objects.select_related("breed", "owner").all()
    serializer_class = KittenListRetrieveSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(summary="Creating the kittens.")
class KittenCreateAPIView(CreateAPIView):
    """Endpoint for creating a kitten."""

    serializer_class = KittenCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        Method for creating a kitten.

        :param request: data from request
        :return: response data
        """

        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@extend_schema(summary="Updating the kitten.")
class KittenUpdateAPIView(UpdateAPIView):
    """Endpoint for updating a kitten."""

    serializer_class = KittenCreateUpdateSerializer
    queryset = Kitten.objects.select_related("breed", "owner").all()
    permission_classes = [IsAuthenticated, IsOwner]

    def update(self, request, *args, **kwargs):
        """
        Method for updating a kitten.

        :param request: data from request
        :return: response data
        """

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


@extend_schema(summary="Deleting a kitten.")
class KittenDestroyAPIView(DestroyAPIView):
    """Endpoint for deleting a kitten."""

    serializer_class = KittenListRetrieveSerializer
    queryset = Kitten.objects.select_related("breed", "owner").all()
    permission_classes = [IsAuthenticated, IsOwner]
