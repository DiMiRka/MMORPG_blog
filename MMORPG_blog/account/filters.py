from django_filters import FilterSet, CharFilter, DateFilter, ChoiceFilter, BooleanFilter
from django import forms

from board.models import Category, Post


class PostFilter(FilterSet):
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


class ResponsesFilter(FilterSet):
    post = ChoiceFilter(field_name='post__name', choices=[], lookup_expr='icontains', label='Пост')
    time_in = DateFilter(field_name='time_in', label='Дата', lookup_expr='gte',
                         widget=forms.DateInput(attrs={'type': 'date'}))
    accepted = BooleanFilter()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['post'].extra['choices'] = [
            (post, post)
            for post in Post.objects.values_list('name', flat=True).distinct()
            ]
