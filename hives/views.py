from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddHiveForm, editHiveForm, addHiveDocumentsForm
from .models import Apiary_details, hive_details, hiveDocuments
from django.contrib import messages


def hive(request, apiary_id):
    """ A view to display the Users list of hives page """
    apiaryID = apiary_id
    hives = hive_details.objects.filter(apiary_id=apiaryID)
    context = {
        'apiaryID': apiaryID,
        'hives': hives,
    }
    return render(request, 'hives/hive.html', context)


def addHive(request, apiary_id, pk=None):
    """ A view to display the add hives page """
    ap = apiary_id
    # get an instance of the apiary pk
    instofID = get_object_or_404(Apiary_details, id=apiary_id)
    hive_details = get_object_or_404(hive, pk=pk) if pk else None
    if request.method == 'POST':
        form = AddHiveForm(request.POST)
        if form.is_valid():
            hive_details = form.save(commit=False)
            hive_details.user = request.user.id
            hive_details.apiary_id = instofID
            hive_details.save()
            messages.success(request, f'Added {hive_details.hive_name}\
                             To your Apiary')
            return redirect('hive', ap)
        else:
            messages.error(request, 'Your hive was not valid')
    else:
        form = AddHiveForm()
        context = {
            'ap': ap,
            'form': form,
        }
        return render(request, 'hives/addHive.html', context)


def editHive(request, apiaryID, pk=None):
    """ A view to display the Edit hives page """
    ap = apiaryID
    currentApiary = get_object_or_404(Apiary_details, pk=apiaryID)
    edithive = get_object_or_404(hive_details, pk=pk) if pk else None
    if request.method == 'POST':
        form = editHiveForm(request.user, request.POST, instance=edithive)
        if form.is_valid():
            edithive.save()
            new = str(edithive.apiary_id)
            current = str(currentApiary.full_name)
            if new != current:
                messages.success(request, f'Hive: {edithive.hive_name.capitalize()} was\
                     Updated And Moved To Apiary: {edithive.apiary_id}!')
            else:
                messages.success(request, f'Hive: {edithive.hive_name.capitalize()} was\
                             Updated!')
            return redirect('hive', ap)
        else:
            messages.error(request, 'Error Hive Was Not Updated!')
    else:
        # Send in request.user to so the queryset can be set so only the
        # logged in user can see apiarys that belong to them.
        form = editHiveForm(request.user, instance=edithive)
        messages.info(request, f'You are editing\
                      Hive: {edithive.hive_name.capitalize()}!')
        context = {
            'ap': ap,
            'form': form,
        }
        return render(request, 'hives/editHive.html', context)


def deleteHive(request, apiaryID, pk):
    """ A view to delete Hives Sites """
    apiary_id = apiaryID
    nameapiary = get_object_or_404(Apiary_details, pk=apiaryID)
    hivedel = get_object_or_404(hive_details, pk=pk)
    messages.warning(request, f'You have Deleted {hivedel.hive_name} From \
                     Apiary {nameapiary.full_name}')
    hivedel.delete()
    return redirect('hive', apiary_id)


def hiveDocs(request, pk):
    """ A view to display the Hive Documents relevent to the hive PK """
    docs = hiveDocuments.objects.filter(hivenumber=pk)
    hivename = get_object_or_404(hive_details, pk=pk)
    context = {
        'docs': docs,
        'hivename': hivename
    }
    return render(request, 'hives/hiveDocs.html', context)


def addhiveDoc(request, pk=None):
    """ A view to display the add Hive Documents """
    instofID = get_object_or_404(hive_details, pk=pk)
    if request.method == 'POST':
        form = addHiveDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            hiveDocuments = form.save(commit=False)
            hiveDocuments.hivenumber = instofID
            hiveDocuments.beekeepername = request.user
            hiveDocuments.save()
            messages.success(request, f'Hive Record Was\
                           Added {instofID.hive_name}')
            return redirect('hiveDocs', pk)
        else:
            messages.error(request, f'Error New Hive Record: {instofID.hive_name} Was\
                           Not Added!')
    else:
        form = addHiveDocumentsForm()
        context = {
            'form': form,
        }
        return render(request, 'hives/addHiveDoc.html', context)


def editHiveDoc(request, hive_id, pk):
    """ A view to display the Edit Hive Documents """
    hiveid = hive_id
    docid = pk
    instdoc = get_object_or_404(hiveDocuments, pk=pk)
    if request.method == 'POST':
        form = addHiveDocumentsForm(request.POST, request.FILES,
                                    instance=instdoc)
        if form.is_valid():
            instdoc.save()
            messages.success(request, f'Log Number: {instdoc.pk} Was\
                             Updated!')
            return redirect('hiveDocs', hiveid)
        else:
            messages.error(request, f'Error Log Number: {instdoc.pk} Was\
                           Not Updated!')
    else:
        form = addHiveDocumentsForm(instance=instdoc)
        messages.info(request, f'You Are Editing {instdoc.pk}!')
        context = {
            'form': form,
            'docid': docid,
            'instdoc': instdoc
        }
        return render(request, 'hives/editHiveDoc.html', context)


def deleteHivedoc(request, hive_id, pk):
    """ A view to delete Hives Sites """
    hiveid = hive_id
    hivedetail = get_object_or_404(hive_details, pk=hive_id)
    hivedocdel = get_object_or_404(hiveDocuments, pk=pk)
    messages.warning(request, f'You Have Deleted Hive Record: {hivedocdel.pk} From\
                     Hive: {hivedetail.hive_name}')
    hivedocdel.delete()
    return redirect('hiveDocs', hiveid)
