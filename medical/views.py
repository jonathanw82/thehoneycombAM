from django.shortcuts import render

# Create your views here.


def beeMedical(request):
    """ A view to display the Wiki page """
    return render(request, 'medical/beeMedical.html')
