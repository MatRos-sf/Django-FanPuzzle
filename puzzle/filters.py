import django_filters
from django import forms

from .models import Puzzle


#https://django-filter.readthedocs.io/en/stable/guide/usage.html
class PuzzleFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr = 'icontains',
        label='Name',
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )
    ean_code = django_filters.CharFilter(
        lookup_expr='exact',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    number_of_pieces = django_filters.NumberFilter(
        lookup_expr='exact',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Puzzle
        fields = ['name', 'ean_code', 'number_of_pieces']
            # {
            # 'name'
            # 'ean_code': ['exact'],
            # 'number_of_pieces': ['exact'],
            # }




