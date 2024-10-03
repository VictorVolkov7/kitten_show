import pytest
from rest_framework import status

from ratings.models import Rating


@pytest.mark.django_db
def test_rating_instance_creation(rating_instance):
    """A test to verify that ratings data has been created correctly."""

    assert rating_instance.pk is not None
    assert isinstance(rating_instance.rating, int)
    assert isinstance(rating_instance.kitten, object)
    assert isinstance(rating_instance.user, object)


@pytest.mark.django_db
def test_rating_string_representation(rating_instance):
    """A test to check the string representation."""

    assert str(rating_instance) == (
        f"{rating_instance.rating} star{'s' if rating_instance.rating > 1 else ''}"
        f" for the {rating_instance.kitten.name} by {rating_instance.user.email}"
    )


@pytest.mark.django_db
def test_rating_create(api_client, kitten_instance, user_instance_1):
    """Test to create kitten rating."""

    user = user_instance_1
    kitten = kitten_instance

    api_client.force_authenticate(user=user)

    data = {
        "rating": 5,
    }
    response = api_client.post(f"/api/kitten/{kitten.pk}/rate/", data)

    assert response.status_code == status.HTTP_201_CREATED
    assert Rating.objects.count() == 1
    assert Rating.objects.get(user=user)
    assert Rating.objects.get(kitten=kitten)
