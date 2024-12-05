from django.urls import path
from django.contrib.auth.views import LoginView

from .views import IndexView, RegisterView, logout_view, onetime_code, MyPostsList

urlpatterns = [
    path('', IndexView.as_view(), name='account'),
    path('register/', RegisterView.as_view(template_name='account/register.html'), name='register'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('onetime_code/', onetime_code, name='onetime_code'),
    path('posts/', MyPostsList.as_view(), name='account_posts')
]
