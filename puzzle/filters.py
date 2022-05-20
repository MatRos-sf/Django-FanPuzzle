import django_filters
from .models import Puzzle

#https://django-filter.readthedocs.io/en/stable/guide/usage.html
class PuzzleFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Puzzle
        fields = {
            'name': ['icontains'],
            'ean_code': ['exact']
            }