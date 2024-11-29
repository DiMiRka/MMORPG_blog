from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets, permissions

from .models import *
from .forms import PostForm, PostsResponsesForm
from .filters import PostFilter
from .serializers import PostsSerializer, CategorySerializer


class CreatePostsResponses(CreateView):
    model = PostsResponses
    form_class = PostsResponsesForm
    template_name = 'post.html'


class CategoriesList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'posts.html'


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
        context['categories'] = Category.objects.all()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = PostsResponsesForm(request.POST)
        if form.is_valid():
            replay = form.save(commit=False)
            replay.post = post
            replay.author = request.user
            replay.save()
            return redirect('post_detail', pk=post.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        post_responses = post.postsresponses_set.all()
        context['form'] = PostsResponsesForm
        context['responses'] = post_responses
        return context


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

