from django.contrib import admin

from .models import Blog, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
