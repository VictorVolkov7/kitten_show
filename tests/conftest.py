import pytest
from rest_framework.test import APIClient

from tests.factories import BreedFactory, UserFactory, KittenFactory, RatingFactory


@pytest.fixture
def breed_instance():
    """Fixture for creating a breed instance."""
    return BreedFactory()


@pytest.fixture
def api_client():
    """
    Fixture for creating an API client instance.

    Client for sending HTTP requests to the Django API
    """
    return APIClient()


@pytest.fixture
def user_instance_1():
    """Fixture for creating a user instance."""
    return UserFactory()


@pytest.fixture
def user_instance_2():
    """Fixture for creating a user instance."""
    return UserFactory()


@pytest.fixture
def kitten_instance():
    """Fixture for creating a kitten instance."""
    return KittenFactory()


@pytest.fixture
def rating_instance():
    """Fixture for creating a rating instance."""
    return RatingFactory()
