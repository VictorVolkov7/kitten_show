import factory
from faker import Faker
from factory.django import DjangoModelFactory

from breeds.models import Breed
from kittens.models import Kitten
from ratings.models import Rating
from users.models import User

fake = Faker()


class UserFactory(DjangoModelFactory):
    """
    Factory for creating test data for users.

    With using faker to generate random data.
    """

    email = factory.LazyAttribute(lambda _: fake.email())
    password = factory.PostGenerationMethodCall("set_password", "password")

    class Meta:
        model = User
        skip_postgeneration_save = True


class BreedFactory(DjangoModelFactory):
    """
    Factory for creating test data for breeds.

    With using faker to generate random data.
    """

    breed_name = fake.word()
    description = fake.text()

    class Meta:
        model = Breed


class KittenFactory(DjangoModelFactory):
    """
    Factory for creating test data for kittens.

    With using faker to generate random data.
    """

    name = fake.word()
    age_year = fake.random_int(min=1, max=50)
    age_month = fake.random_int(min=1, max=12)
    breed = factory.SubFactory(BreedFactory)
    color = fake.word()
    description = fake.text()
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = Kitten


class RatingFactory(DjangoModelFactory):
    """
    Factory for creating test data for ratings.

    With using faker to generate random data.
    """

    rating = fake.random_int(min=1, max=5)
    user = factory.SubFactory(UserFactory)
    kitten = factory.SubFactory(KittenFactory)

    class Meta:
        model = Rating
