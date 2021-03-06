# blog URL Configuration

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('bloggers/<int:pk>/',
         views.BloggerDetailView.as_view(), name='blogger_detail'),
    path('blog/<int:pk>/create', views.CommentAdd.as_view(), name='add_comment'),
]
