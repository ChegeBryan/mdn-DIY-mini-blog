from django.shortcuts import render
from django.views.generic import ListView

from .models import Blog


def index(request):
    """ View function for home page of site """

    # Render the HTML temlate ,index.html
    return render(request, 'index.html')


class BlogListView(ListView):
    model = Blog
    paginate_by = 5
