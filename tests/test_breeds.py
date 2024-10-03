import pytest
from rest_framework import status


@pytest.mark.django_db
def test_breed_instance_creation(breed_instance):
    """A test to verify that breed data has been created correctly."""

    assert breed_instance.pk is not None
    assert isinstance(breed_instance.breed_name, str)
    assert isinstance(breed_instance.description, str)


@pytest.mark.django_db
def test_breed_string_representation(breed_instance):
    """A test to check the string representation."""

    assert str(breed_instance) == breed_instance.breed_name


@pytest.mark.django_db
def test_breed_list(api_client, breed_instance, user_instance_1):
    """Test to check the endpoint of obtaining a list of breeds."""

    api_client.force_authenticate(user=user_instance_1)

    response = api_client.get("/api/breeds/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0


@pytest.mark.django_db
def test_breed_list_unauthenticated(api_client):
    """A test to check that unauthenticated users cannot access the breed list."""

    response = api_client.get("/api/breeds/")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
