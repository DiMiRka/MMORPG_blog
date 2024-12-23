from django import template
from bs4 import BeautifulSoup

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


@register.filter()
def text_preview(value):
    if not value:
        return ""
    soup = BeautifulSoup(value, 'html.parser')
    for img in soup.find_all('img'):
        img.decompose()
    text = soup.get_text()
    return text


@register.filter()
def img_preview(value):
    if not value:
        return ""
    soup = BeautifulSoup(value, 'html.parser')
    new = soup.find('img')
    return new
