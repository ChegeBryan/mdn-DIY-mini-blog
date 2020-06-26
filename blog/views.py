from django.shortcuts import render, get_object_or_404
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog"] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context
