from django.urls import path
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

from .views import IndexView, RegisterView, logout_view, onetime_code, MyPostsList, response_accept, response_delete

urlpatterns = [
    path('', IndexView.as_view(), name='account'),
    path('register/', RegisterView.as_view(template_name='account/register.html'), name='register'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('onetime_code/', onetime_code, name='onetime_code'),
    path('code_error/', TemplateView.as_view(template_name='account/code_error.html'), name='code_error'),
    path('posts/', MyPostsList.as_view(), name='account_posts'),
    path('<int:pk>/accept', response_accept, name='response_accept'),
    path('<int:pk>/delete', response_delete, name='response_delete'),
]
