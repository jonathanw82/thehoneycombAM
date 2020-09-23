from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import AddHiveForm
from .models import Apiary_details
from .models import hive_details

# Create your views here.


def hive(request, apiary_id):
    """ A view to display the Users list of hives page """
    apiaryID = apiary_id
    hives = hive_details.objects.filter(apiary_id=apiaryID)
    context = {
        'apiaryID': apiaryID,
        'hives': hives,
    }
    return render(request, 'hives/hive.html', context)


def addHive(request, apiaryID, pk=None):
    """ A view to display the add hives page """
    ap = apiaryID
    hive_details = get_object_or_404(hive, pk=pk) if pk else None
    if request.method == 'POST':
        form = AddHiveForm(request.POST)
        if form.is_valid():
            hive_details = form.save(commit=False)
            hive_details.user = request.user.id
            hive_details.apiary_id = ap
            hive_details.save()
            return redirect('hive', ap)
    else:
        form = AddHiveForm()
        context = {
            'ap': ap,
            'form': form,
        }
        return render(request, 'hives/addHive.html', context)


def deleteHive(request, pk, apiary_id):
    """ A view to delete Hives Sites """
    hivedel = get_object_or_404(hive_details, pk=pk)
    hivedel.delete()
    return redirect('hive', apiary_id)
