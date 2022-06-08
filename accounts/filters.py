import django_filters
from django import forms
from .models import Account

###########################################################################################################
#                       USER
###########################################################################################################

class UserFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(
        lookup_expr='exact',
        label='Email',
        widget=forms.TextInput(attrs={'class': 'form-control'})

    )
    username = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'})

    )
    class Meta:
        model = Account
        fields = ['email', 'username']