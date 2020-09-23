from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddApiaryForm
from .models import Apiary_details

# Create your views here.


def setup(request):
    """ A view to display the Wiki page """
    return render(request, 'apiary/setup.html')


def apiary(request):
    """ A view to display the Users list of Apiarys page """
    apiaries = Apiary_details.objects.all()
    context = {
        'apiaries': apiaries,
    }
    return render(request, 'apiary/apiary.html', context)


def addApiary(request, pk=None):
    """ A view to display the add Apiary page """
    if request.method == 'POST':
        form = AddApiaryForm(request.POST)
        if form.is_valid():
            Apiary_details = form.save(commit=False)
            Apiary_details.user = request.user
            Apiary_details.save()
            return redirect('apiary')
    else:
        form = AddApiaryForm()
        context = {
            'form': form,
        }
    return render(request, 'apiary/addApiary.html', context)


def editApiary(request, pk=None):
    """ A view to editing Apiary Sites """
    editapiary = get_object_or_404(Apiary_details, pk=pk) if pk else None
    if request.method == 'POST':
        form = AddApiaryForm(request.POST, instance=editapiary)
        if form.is_valid():
            editapiary = form.save(commit=False)
            editapiary.user = request.user
            editapiary.save()
            return redirect('apiary')
    else:
        form = AddApiaryForm(instance=editapiary)
        context = {
            'form': form,
        }
    return render(request, 'apiary/editApiary.html', context)


def deleteApiary(request, pk):
    """ A view to delete Apiary Sites """
    apiarydel = get_object_or_404(Apiary_details, pk=pk)
    apiarydel.delete()
    return redirect('apiary')
