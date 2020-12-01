from django.shortcuts import render


def index(request):
    """ A view to display the index page """
    if request.user.is_authenticated:
        return render(request, 'home/loggedInUser.html')
    else:
        return render(request, 'home/index.html')


def userLoggedIn(request):
    """ A view to display the index page """
    return render(request, 'home/loggedInUser.html')


def wiki(request):
    """ A view to display the Wiki page """
    return render(request, 'home/wiki.html')
