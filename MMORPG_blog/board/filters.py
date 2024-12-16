from django_filters import FilterSet, CharFilter, DateFilter, ChoiceFilter
from django import forms
from django.contrib.auth.models import User

from .models import Category


class PostFilter(FilterSet):
    author = CharFilter(field_name='author__username', lookup_expr='icontains', label='Автор')
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Название')
    time_in = DateFilter(field_name='time_in', label='Дата', lookup_expr='gte',
                         widget=forms.DateInput(attrs={'type': 'date'}))


