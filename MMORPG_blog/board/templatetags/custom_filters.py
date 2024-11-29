from django import template

from ..models import Post

register = template.Library()


@register.filter()
def len_category(value):
    categories = Post.objects.filter(category__name=value)
    return len(categories)
