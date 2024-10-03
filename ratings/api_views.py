from drf_spectacular.utils import extend_schema
from rest_framework import generics, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from kittens.models import Kitten
from ratings.serializers import RatingCreateSerializer


@extend_schema(summary="Creating the rating.")
class RatingCreateAPIView(generics.CreateAPIView):
    serializer_class = RatingCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """
        Addition for creating a rating.

        :param serializer: rating serializer
        """
        kitten_id = self.kwargs.get("pk")

        try:
            kitten = Kitten.objects.get(pk=kitten_id)
            serializer.save(user=self.request.user, kitten=kitten)
        except Kitten.DoesNotExist:
            raise serializers.ValidationError({"error": "Kitten not found."})

    def post(self, request, *args, **kwargs):
        """
        Processes HTTP POST request.

        Gets the rating of the data, serializes
        and returns the response.
        :param request: request data
        :return: response data
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
