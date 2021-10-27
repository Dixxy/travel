from django.contrib import admin

from blog.models import PostModel, NewModel, CommentModel


@admin.register(PostModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', ]
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(NewModel)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'created_at', ]
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['phone', 'created_at', 'name', 'email', 'comment']
    list_filter = ['created_at', 'phone']
    search_fields = ['name']
