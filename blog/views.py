from django.shortcuts import render


def index(request):
    """ View function for home page of site """

    # Render the HTML temlate ,index.html
    return render(request, 'index.html')
