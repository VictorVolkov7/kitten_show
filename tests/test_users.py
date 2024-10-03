import pytest
from rest_framework import status

from users.models import User


@pytest.mark.django_db
def test_user_instance_creation(user_instance_1):
    """A test to verify that users data has been created correctly."""

    assert user_instance_1.pk is not None
    assert isinstance(user_instance_1.email, str)


@pytest.mark.django_db
def test_user_string_representation(user_instance_1):
    """A test to check the string representation."""

    assert (
        str(user_instance_1)
        == f"{user_instance_1.first_name} {user_instance_1.last_name} - {user_instance_1.email}"
    )


@pytest.mark.django_db
def test_user_create(api_client):
    """Test to create user."""

    data = {
        "email": "test@mail.ru",
        "password": "test1212",
    }
    response = api_client.post(f"/api/register/", data)

    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.count() == 1
    assert User.objects.get(email="test@mail.ru")


@pytest.mark.django_db
def test_user_create_incorrect(api_client):
    """Test to create user with incorrect data."""

    data = {
        "email": "test12mail1ru",
        "password": "test1212",
    }
    response = api_client.post(f"/api/register/", data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_get_tokens(api_client, user_instance_1):
    """Test to get access/refresh token."""

    user = user_instance_1

    user.set_password("test1212")
    user.save()

    data = {"email": user.email, "password": "test1212"}
    response = api_client.post(f"/api/token/", data)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["access"]
    assert response.data["refresh"]


@pytest.mark.django_db
def test_get_refresh_token(api_client, user_instance_1):
    """Test to get refresh token."""

    user = user_instance_1

    user.set_password("test1212")
    user.save()

    data = {"email": user.email, "password": "test1212"}
    response = api_client.post(f"/api/token/", data)
    refresh_token = response.data["refresh"]

    data = {"refresh": refresh_token}
    response = api_client.post(f"/api/token/refresh/", data)

    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
    assert response.data["access"]
