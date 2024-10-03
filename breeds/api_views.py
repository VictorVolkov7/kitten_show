from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from breeds.models import Breed
from breeds.serializers import BreedListSerializer


@extend_schema(summary="Viewing the list of breeds.")
class BreedListAPIView(generics.ListAPIView):
    """Endpoint for viewing the list of breeds."""

    serializer_class = BreedListSerializer
    queryset = Breed.objects.all()
    permission_classes = [IsAuthenticated]
