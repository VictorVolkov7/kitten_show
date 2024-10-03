import pytest
from rest_framework import status

from kittens.models import Kitten


@pytest.mark.django_db
def test_kitten_instance_creation(kitten_instance):
    """A test to verify that kittens data has been created correctly."""

    assert kitten_instance.pk is not None
    assert isinstance(kitten_instance.name, str)
    assert isinstance(kitten_instance.age_year, int)
    assert isinstance(kitten_instance.age_month, int)
    assert isinstance(kitten_instance.breed, object)
    assert isinstance(kitten_instance.color, str)
    assert isinstance(kitten_instance.description, str)
    assert isinstance(kitten_instance.owner, object)


@pytest.mark.django_db
def test_kitten_string_representation(kitten_instance):
    """A test to check the string representation."""

    assert str(kitten_instance) == (
        f"Kitten {kitten_instance.name} of the {kitten_instance.breed} breed, "
        f"{kitten_instance.age_year} year and {kitten_instance.age_month} month old."
    )


@pytest.mark.django_db
def test_kitten_list(api_client, kitten_instance, user_instance_1):
    """Test to check the endpoint of obtaining a list of kittens."""

    api_client.force_authenticate(user=user_instance_1)
    response = api_client.get("/api/kittens/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0


@pytest.mark.django_db
def test_kitten_list_unauthenticated(api_client):
    """A test to check that unauthenticated users cannot access the kitten list."""

    response = api_client.get("/api/kittens/")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_kitten_retrieve(api_client, kitten_instance, user_instance_1):
    """Test to check the endpoint of obtaining a kitten."""

    kitten = kitten_instance

    api_client.force_authenticate(user=user_instance_1)

    response = api_client.get(f"/api/kitten/{kitten.pk}/")

    assert response.status_code == status.HTTP_200_OK
    assert Kitten.objects.get(pk=kitten.pk).name == kitten.name


@pytest.mark.django_db
def test_kitten_retrieve_unauthenticated(api_client, kitten_instance):
    """A test to check that unauthenticated users cannot access of obtaining a kitten."""

    kitten = kitten_instance

    response = api_client.get(f"/api/kitten/{kitten.pk}/")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_kitten_delete_own(api_client, kitten_instance, user_instance_1):
    """Test to remove your kitten."""

    user = user_instance_1
    kitten = kitten_instance

    kitten.owner = user
    kitten.save()

    api_client.force_authenticate(user=user)

    response = api_client.delete(f"/api/kitten/{kitten.pk}/delete/")

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Kitten.objects.count() == 0


@pytest.mark.django_db
def test_kitten_delete_stranger(
    api_client, kitten_instance, user_instance_1, user_instance_2
):
    """Test to remove stranger kitten."""

    user_1 = user_instance_1
    user_2 = user_instance_2
    kitten = kitten_instance

    kitten.owner = user_1
    kitten.save()

    api_client.force_authenticate(user=user_2)

    response = api_client.delete(f"/api/kitten/{kitten.pk}/delete/")

    assert user_1 != user_2
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_kitten_delete_unauthenticated(api_client, kitten_instance):
    """A test to check that unauthenticated users cannot access to remove kitten."""

    kitten = kitten_instance

    response = api_client.delete(f"/api/kitten/{kitten.pk}/delete/")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_kitten_patch_own(api_client, kitten_instance, user_instance_1):
    """Test to update your kitten."""

    user = user_instance_1
    kitten = kitten_instance

    kitten.owner = user
    kitten.save()

    api_client.force_authenticate(user=user)

    data = {"name": "Васька"}
    response = api_client.patch(f"/api/kitten/{kitten.pk}/update/", data)

    assert response.status_code == status.HTTP_200_OK
    assert Kitten.objects.get(pk=kitten.pk).name == "Васька"


@pytest.mark.django_db
def test_kitten_patch_stranger(
    api_client, kitten_instance, user_instance_1, user_instance_2
):
    """Test to update stranger kitten."""

    user_1 = user_instance_1
    user_2 = user_instance_2
    kitten = kitten_instance

    kitten.owner = user_1
    kitten.save()

    api_client.force_authenticate(user=user_2)

    data = {"name": "Васька"}
    response = api_client.patch(f"/api/kitten/{kitten.pk}/update/", data)

    assert user_1 != user_2
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_kitten_patch_unauthenticated(api_client, kitten_instance):
    """A test to check that unauthenticated users cannot access to patch kitten."""

    kitten = kitten_instance

    response = api_client.patch(f"/api/kitten/{kitten.pk}/update/")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_kitten_patch_own_incorrect(api_client, kitten_instance, user_instance_1):
    """Test to update your kitten with incorrect data."""

    user = user_instance_1
    kitten = kitten_instance

    kitten.owner = user
    kitten.save()

    api_client.force_authenticate(user=user)

    data = {"name": "Васька", "age_year": "", "age_month": ""}
    response = api_client.patch(f"/api/kitten/{kitten.pk}/update/", data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_kitten_put_own(api_client, kitten_instance, breed_instance, user_instance_1):
    """Test to put your kitten."""

    user = user_instance_1
    kitten = kitten_instance
    breed = breed_instance

    kitten.owner = user
    kitten.save()

    api_client.force_authenticate(user=user)

    data = {
        "name": "Васька",
        "age_year": 2,
        "age_month": "",
        "breed": breed.pk,
        "color": "string",
        "description": "string",
    }
    response = api_client.put(f"/api/kitten/{kitten.pk}/update/", data)

    assert response.status_code == status.HTTP_200_OK
    assert Kitten.objects.get(pk=kitten.pk).name == "Васька"


@pytest.mark.django_db
def test_kitten_put_stranger(
    api_client, kitten_instance, user_instance_1, user_instance_2, breed_instance
):
    """Test to put stranger kitten."""

    user_1 = user_instance_1
    user_2 = user_instance_2
    kitten = kitten_instance
    breed = breed_instance

    kitten.owner = user_1
    kitten.save()

    api_client.force_authenticate(user=user_2)

    data = {
        "name": "Васька",
        "age_year": 2,
        "age_month": "",
        "breed": breed.pk,
        "color": "string",
        "description": "string",
    }
    response = api_client.put(f"/api/kitten/{kitten.pk}/update/", data)

    assert user_1 != user_2
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_kitten_put_unauthenticated(api_client, kitten_instance):
    """A test to check that unauthenticated users cannot access to put kitten."""

    kitten = kitten_instance

    response = api_client.put(f"/api/kitten/{kitten.pk}/update/")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_kitten_put_own_incorrect(
    api_client, kitten_instance, user_instance_1, breed_instance
):
    """Test to put your kitten with incorrect data."""

    user = user_instance_1
    kitten = kitten_instance
    breed = breed_instance

    kitten.owner = user
    kitten.save()

    api_client.force_authenticate(user=user)

    data = {
        "name": "Васька",
        "age_year": "",
        "age_month": "",
        "breed": breed.pk,
        "color": "string",
        "description": "string",
    }
    response = api_client.patch(f"/api/kitten/{kitten.pk}/update/", data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_kitten_create(api_client, breed_instance, user_instance_1):
    """Test to create your kitten."""

    user = user_instance_1
    breed = breed_instance

    api_client.force_authenticate(user=user)

    data = {
        "name": "Васька",
        "age_year": 2,
        "age_month": "",
        "breed": breed.pk,
        "color": "string",
        "description": "string",
    }
    response = api_client.post(f"/api/kitten/create/", data)

    assert response.status_code == status.HTTP_201_CREATED
    assert Kitten.objects.count() == 1
    assert Kitten.objects.get(name="Васька")
    assert Kitten.objects.get(owner=user)


@pytest.mark.django_db
def test_kitten_create_unauthenticated(api_client):
    """A test to check that unauthenticated users cannot access to put kitten."""

    response = api_client.post(f"/api/kitten/create/")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_kitten_put_own_incorrect(api_client, user_instance_1, breed_instance):
    """Test to put your kitten with incorrect data."""

    user = user_instance_1
    breed = breed_instance

    api_client.force_authenticate(user=user)

    data = {
        "name": "Васька",
        "age_year": "",
        "age_month": "",
        "breed": breed.pk,
        "color": "string",
        "description": "string",
    }
    response = api_client.post(f"/api/kitten/create/", data)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
