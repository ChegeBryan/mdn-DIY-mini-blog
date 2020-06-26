from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Blog, Blogger, Comment


def index(request):
    """ View function for home page of site """

    # Render the HTML temlate ,index.html
    return render(request, 'index.html')


class BlogListView(ListView):
    model = Blog
    paginate_by = 5


class BlogDetailView(DetailView):
    model = Blog


class BloggerListView(ListView):
    model = Blogger


class BloggerDetailView(DetailView):
    model = Blogger


class CommentAdd(CreateView):
    model = Comment
    fields = ['comment']
