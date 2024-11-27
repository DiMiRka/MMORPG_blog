from django.contrib import admin

from .models import Post, Category, PostsResponses, PostCategory


class CategoryAdmin(admin.TabularInline):
    model = PostCategory
    extra = 1


class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = (CategoryAdmin,)
    list_display = ('name', 'author', 'get_category', 'time_in')
    list_filter = ('name', 'author', 'category__name')
    search_fields = ('name', 'category__name', 'author__user__username')


class ResponseAdmin(admin.ModelAdmin):
    model = PostsResponses
    list_display = ('author', 'text', 'time_in', 'accepted')
    list_filter = ('author', 'time_in', 'accepted')
    search_fields = ('author__user__username',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(PostsResponses, ResponseAdmin)
