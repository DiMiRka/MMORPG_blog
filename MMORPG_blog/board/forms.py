from django import forms

from .models import Post, PostsResponses


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'name', 'text']


class PostsResponsesForm(forms.ModelForm):
    class Meta:
        model = PostsResponses
        fields = ['text',]
        labels = {
            'text': 'Введите текст отклика',
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-text', 'cols': 300, 'rows': 2, 'style': 'background:gray; border:solid 5px green'})
        }
