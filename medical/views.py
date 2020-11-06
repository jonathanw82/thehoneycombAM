from django.shortcuts import render, redirect, get_object_or_404
from .forms import addHiveMedicineForm, addHiveMedicalRecordForm
from .models import hiveMedical, hiveMedicalRecords
from hives.models import hive_details
from django.contrib import messages
from datetime import date
from django.utils import timezone


def beeMedical(request):
    """ A view to display the Bee medical page """
    datetoday = date.today()
    user = request.user
    medications = hiveMedical.objects.filter(user=user)
    context = {
        'medications': medications,
        'datetoday': datetoday
    }
    return render(request, 'medical/beeMedical.html', context)


def addMedicine(request, pk=None):
    """ A view to display the add medicine page """
    if request.method == 'POST':
        form = addHiveMedicineForm(request.POST)
        if form.is_valid():
            hiveMedical = form.save(commit=False)
            hiveMedical.user = request.user
            hiveMedical.save()
            return redirect('beeMedical')
        else:
            messages.error(request, 'Your medicine form was not valid')
    else:
        form = addHiveMedicineForm()
        context = {
            'form': form,
        }
        return render(request, 'medical/addMedicine.html', context)


def editMedicine(request, pk=None):
    """ A view to display the add medicine page """
    editMedicine = get_object_or_404(hiveMedical, pk=pk)
    if request.method == 'POST':
        form = addHiveMedicineForm(request.POST, instance=editMedicine)
        if form.is_valid():
            editMedicine = form.save(commit=False)
            editMedicine.medicine_updated = timezone.now()
            editMedicine.save()
            return redirect('beeMedical')
        else:
            messages.error(request, 'Your medicine form was not valid')
    else:
        form = addHiveMedicineForm(instance=editMedicine)
        context = {
            'form': form,
        }
        return render(request, 'medical/editMedicine.html', context)


def deleteMedicine(request, pk):
    """ A view to delete Medicine """
    medicineDel = get_object_or_404(hiveMedical, pk=pk)
    messages.warning(request, f'You Have Deleted {medicineDel.medicine_name}')
    medicineDel.delete()
    return redirect('beeMedical')


def hiveMedicalHistory(request, pk):
    hiveinst = get_object_or_404(hive_details, pk=pk)
    medications = hiveMedicalRecords.objects.filter(hivenumber=hiveinst.pk)
    context = {
        'medications': medications,
        'hiveinst': hiveinst
    }
    return render(request, 'medical/hiveMedicalHistory.html', context)


def addMedicalRecord(request, pk=None):
    """ A view to display the add medicine page """
    user = request.user
    isMedicinePresent = hiveMedical.objects.filter(user=user)
    hiveinst = get_object_or_404(hive_details, pk=pk)
    if request.method == 'POST':
        form = addHiveMedicalRecordForm(user, request.POST)
        if form.is_valid():
            hiveMedicalRecords = form.save(commit=False)
            hiveMedicalRecords.hivenumber = hiveinst
            hiveMedicalRecords.hive_name = hiveinst.hive_name
            hiveMedicalRecords.save()
            return redirect('hiveMedicalHistory', pk)
        else:
            messages.error(request, 'Your medical record was not valid')
    else:
        form = addHiveMedicalRecordForm(user)
        context = {
            'form': form,
            'hiveinst': hiveinst,
            'isMedicinePresent': isMedicinePresent
        }
        return render(request, 'medical/addMedicalRecord.html', context)


def editMedicalRecord(request, hiveinst_id, pk=None):
    """ A view to display the add medicine page """
    user = request.user
    hiveinst = get_object_or_404(hive_details, pk=hiveinst_id)
    editMedicineRecord = get_object_or_404(hiveMedicalRecords, pk=pk)
    if request.method == 'POST':
        form = addHiveMedicalRecordForm(user, request.POST,
                                        instance=editMedicineRecord)
        if form.is_valid():
            editMedicineRecord = form.save(commit=False)
            editMedicineRecord.medicine_updated = timezone.now()
            editMedicineRecord.save()
            return redirect('hiveMedicalHistory', hiveinst_id)
        else:
            messages.error(request, 'Your medical record was not valid')
    else:
        form = addHiveMedicalRecordForm(user, instance=editMedicineRecord)
        context = {
            'form': form,
            'hiveinst': hiveinst,
        }
        return render(request, 'medical/editMedicalRecord.html', context)


def deleteMedicalRecord(request, hiveinst_id, pk):
    """ A view to delete Medicine """
    recordDel = get_object_or_404(hiveMedicalRecords, pk=pk)
    messages.warning(request, f'You Have Deleted The Medical Record\
                     Number:{ recordDel.pk }')
    recordDel.delete()
    return redirect('hiveMedicalHistory', hiveinst_id)
