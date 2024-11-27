from django_filters import FilterSet, CharFilter, DateFilter, ChoiceFilter
from django import forms
from django.contrib.auth.models import User

from .models import Category


class PostFilter(FilterSet):
    author = CharFilter(field_name='author__username', lookup_expr='icontains', label='Автор')
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Название')
    category = ChoiceFilter(field_name='category__name', choices=[], lookup_expr='icontains', label='Категория')
    time_in = DateFilter(field_name='time_in', label='Дата', lookup_expr='gte',
                         widget=forms.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['category'].extra['choices'] = [
            (category, category)
            for category in Category.objects.values_list('name', flat=True).distinct()
        ]
