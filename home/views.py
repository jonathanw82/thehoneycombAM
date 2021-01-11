from django.shortcuts import render, redirect


def index(request):
    """ A view to display the index page """
    if request.user.is_authenticated:
        # go to apiarys page if already logged in.
        return redirect("apiary")
    else:
        return render(request, 'home/index.html')


def wiki(request):
    """ A view to display the Wiki page """
    return render(request, 'home/Wiki.html')
