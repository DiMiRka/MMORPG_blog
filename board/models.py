from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


class Category(models.Model):
    """Модель категории постов"""
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Модель постов"""
    author = models.ForeignKey(verbose_name='Автор', to=User, on_delete=models.CASCADE, db_index=True)
    time_in = models.DateField(auto_now_add=True)
    name = models.CharField(verbose_name='Заголовок', max_length=50, default='no name')
    text = HTMLField(verbose_name='Текст')
    category = models.ManyToManyField(Category, verbose_name='Категория', through='PostCategory', blank=False,
                                      related_name='category', db_index=True)

    def get_category(self):
        return ",".join([str(c) for c in self.category.all()])

    get_category.short_description = 'Категория'

    def get_response(self):
        return ','.join([str(p) for p in PostsResponses.objects.filter(post=self.pk, accept=True)])

    def preview(self):
        return f'{self.text[:80]}...'

    def __str__(self):
        return f'{self.name.title()}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    """Связь между постами и категориями"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class PostsResponses(models.Model):
    """Модель представления постов"""
    author = models.ForeignKey(verbose_name='Автор', to=User, on_delete=models.CASCADE, db_index=True)
    post = models.ForeignKey(verbose_name='Объявление', to=Post, on_delete=models.CASCADE, db_index=True)
    text = models.CharField(verbose_name='Текст', max_length=400)
    time_in = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.post.pk), ))
