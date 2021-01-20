from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddApiaryForm
from .models import Apiary_details
import datetime

# Create your views here.


# @login_required
# def setup(request):
#     """ A view to display the Wiki page """
#     return render(request, 'apiary/setup.html')


@login_required
def apiary(request):
    """ A view to display the Users list of Apiarys page """
    dt = datetime.datetime.today()
    month = dt.month
    user = request.user
    apiaries = Apiary_details.objects.filter(user=user)
    context = {
        'apiaries': apiaries,
        'month': month,
    }
    return render(request, 'apiary/apiary.html', context)


@login_required
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


@login_required
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


@login_required
def deleteApiary(request, pk):
    """ A view to delete Apiary Sites """
    apiarydel = get_object_or_404(Apiary_details, pk=pk)
    if request.method == 'POST':
        apiarydel.delete()
        return redirect('apiary')
    context = {
        "apiarydel": apiarydel
    }
    return render(request, 'apiary/confirm_delete.html', context)
