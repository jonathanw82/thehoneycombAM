from django.shortcuts import render


def index(request):
    """ A view to display the index page """
    return render(request, 'home/index.html')


def wiki(request):
    """ A view to display the Wiki page """
    return render(request, 'home/Wiki.html')
