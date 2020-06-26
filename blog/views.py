import datetime

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

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        # Add logged-in user as author of comment
        form.instance.author = self.request.user
        # Associate comment with blog based on passed id
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        # Add current time to form
        form.instance.post_date = datetime.datetime.now()
        # Call super-class form validation behaviour
        return super().form_valid(form)
