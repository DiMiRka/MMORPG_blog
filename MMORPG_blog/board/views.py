from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import *
from .forms import PostForm
from .filters import PostFilter



class PostsList(ListView):
    model = Post
    ordering = '-time_in'
    context_object_name = 'posts'
    template_name = 'posts.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'


class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'


class DeletePost(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')
