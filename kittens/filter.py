import django_filters

from kittens.models import Kitten


class BreedFilter(django_filters.FilterSet):
    """Custom filter to search for kittens by breed."""

    breed = django_filters.CharFilter(field_name="breed", lookup_expr="exact")

    class Meta:
        model = Kitten
        fields = ("breed",)
