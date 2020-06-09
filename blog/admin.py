from django.contrib import admin

from .models import Blog, Comment, Blogger


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date')
    inlines = [CommentInline, ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'author', 'post_date')


admin.site.register(Blogger)
