from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('posts/', include('board.urls')),
    path('account/', include('account.urls')),
    path('', include('board.urls')),
    path('tinymce/', include('tinymce.urls')),
]

