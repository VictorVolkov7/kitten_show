from django.urls import path

from ratings.api_views import RatingCreateAPIView
from ratings.apps import RatingsConfig

app_name = RatingsConfig.name

urlpatterns = [
    path(
        "kitten/<int:pk>/rate/",
        RatingCreateAPIView.as_view(),
        name="kitten-rate"
    ),
]
