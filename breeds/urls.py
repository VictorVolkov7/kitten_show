from django.urls import path

from breeds.api_views import BreedListAPIView
from breeds.apps import BreedsConfig

app_name = BreedsConfig.name

urlpatterns = [
    path("breeds/", BreedListAPIView.as_view(), name="breed-list"),
]
