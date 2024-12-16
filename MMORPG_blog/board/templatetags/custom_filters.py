from django import template

from ..models import Post, PostsResponses

register = template.Library()


@register.filter()
def len_category(value):
    categories = Post.objects.filter(category__name=value)
    return len(categories)


@register.filter()
def len_responses(value):
    responses = PostsResponses.objects.filter(post=value, accepted=True)
    return len(responses)
