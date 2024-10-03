from django.urls import path

from kittens.api_views import (
    KittenListApiView,
    KittenRetrieveAPIView,
    KittenCreateAPIView,
    KittenUpdateAPIView,
    KittenDestroyAPIView,
)
from kittens.apps import KittensConfig

app_name = KittensConfig.name

urlpatterns = [
    path("kittens/", KittenListApiView.as_view(), name="kittens-list"),
    path("kitten/<int:pk>/", KittenRetrieveAPIView.as_view(), name="kitten-info"),
    path("kitten/create/", KittenCreateAPIView.as_view(), name="kitten-create"),
    path(
        "kitten/<int:pk>/update/", KittenUpdateAPIView.as_view(), name="kitten-update"
    ),
    path(
        "kitten/<int:pk>/delete/", KittenDestroyAPIView.as_view(), name="kitten-delete"
    ),
]
