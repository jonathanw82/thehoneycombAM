from django.shortcuts import render, redirect
from .forms import AddApiaryForm
from .models import Apiary_details

# Create your views here.


def setup(request):
    """ A view to display the Wiki page """
    return render(request, 'apiary/setup.html')


def apiary(request):
    """ A view to display the Users list of Apiarys page """
    sites = Apiary_details.objects.all()

    apiary_sites = {
        'sites': sites,
    }
    return render(request, 'apiary/apiary.html', apiary_sites)


def addApiary(request):
    """ A view to display the add Apiary page """
    if request.method == 'POST':
        form = AddApiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('setup')
    else:
        form = AddApiaryForm()
        context = {
            'form': form,
        }
    return render(request, 'apiary/addApiary.html', context)
