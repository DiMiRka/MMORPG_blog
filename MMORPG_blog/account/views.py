import string
import random

from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from account.models import OneTimeCode
from .filters import PostFilter, ResponsesFilter
from .models import RegisterForm
from board.models import Post, Category, PostsResponses
from MMORPG_blog import settings


def generate_string(length):
    all_symbols = string.ascii_uppercase + string.digits
    result = ''.join(random.choice(all_symbols) for _ in range(length))
    return result


class IndexView(ListView):
    template_name = 'account/aclog.html'
    model = PostsResponses
    ordering = '-time_in'
    context_object_name = 'myresponses'

    def get_queryset(self):
        user = self.request.user
        queryset = PostsResponses.objects.filter(post__author__id=user.id)
        self.filterset = ResponsesFilter(self.request.GET, queryset, request=user.id)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['post'] = Post.objects.filter(author=user.id)
        return context


def response_accept(request, pk):
    response = PostsResponses.objects.get(id=pk)
    response.accepted = True
    response.save()

    html_content = render_to_string(
        'account/appointment_accepted.html',
        {
            'link': f'{settings.SITE_URL}/posts/{response.post.id}',
            'name': response.author,
            'post': response.post.name
        }
    )

    msg = EmailMultiAlternatives(
        subject='Ваш отклик был принят',
        body='',
        from_email=settings.EMAIL_ADMIN,
        to=[response.author.email]
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

    return redirect('account')


def response_delete(request, pk):
    response = PostsResponses.objects.get(id=pk)
    response.delete()
    return redirect('account')


class MyPostsList(ListView):
    model = Post
    ordering = '-time_in'
    context_object_name = 'myposts'
    template_name = 'account/acposts.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Post.objects.filter(author__id=user.id)
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['categories'] = Category.objects.all()
        return context


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('onetime_code')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        return super().form_valid(form)


def onetime_code(request):
    if request.method == 'POST':
        code = request.POST['code']
        one_time_code = OneTimeCode.objects.filter(code=code)
        if one_time_code:
            user = one_time_code.first().user
            user.is_active = True
            user.save()
            one_time_code.delete()
            return redirect('login')
        else:
            return redirect('code_error')

    return render(request, 'account/onetime_code.html')


def logout_view(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/posts/')
