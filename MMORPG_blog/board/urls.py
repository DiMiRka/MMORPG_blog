from django.urls import path, include
from .views import PostsList, PostDetail, CreatePost, UpdatePost, DeletePost, CreatePostsResponses


urlpatterns = [
    path('', PostsList.as_view(), name='posts'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', CreatePost.as_view(), name='create_post'),
    path('<int:pk>/update', UpdatePost.as_view(), name='update_post'),
    path('<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
]
