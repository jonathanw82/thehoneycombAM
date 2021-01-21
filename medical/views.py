from django.shortcuts import render, redirect, get_object_or_404
from .forms import addHiveMedicineForm, addHiveMedicalRecordForm
from .models import hiveMedical, hiveMedicalRecords
from django.contrib.auth.decorators import login_required
from hives.models import hive_details
from apiary.models import Apiary_details
from django.contrib import messages
from datetime import date
from django.utils import timezone


@login_required
def beeMedical(request):
    """ A view to display the Bee medical page """
    datetoday = date.today()
    user = request.user
    medications = hiveMedical.objects.filter(user=user)
    context = {
        'medications': medications,
        'datetoday': datetoday,
    }
    return render(request, 'medical/beeMedical.html', context)


def medhiveused(request, medID):
    datetoday = date.today()
    medications = get_object_or_404(hiveMedical, pk=medID)
    medhivesusing = hiveMedicalRecords.objects.filter(medicine_id=medID)
    context = {
        'medhivesusing': medhivesusing,
        'medications': medications,
        'datetoday': datetoday,
    }
    return render(request, 'medical/medhiveused.html', context)


@login_required
def addMedicine(request, pk=None):
    """ A view to display the add medicine page """
    if request.method == 'POST':
        form = addHiveMedicineForm(request.POST)
        if form.is_valid():
            hiveMedical = form.save(commit=False)
            hiveMedical.user = request.user
            hiveMedical.save()
            messages.success(
                request, "You have successfully added a medicine",
            )
            return redirect('beeMedical')
        else:
            messages.error(request, 'Your medicine form was not valid')
    else:
        form = addHiveMedicineForm()
        context = {
            'form': form,
        }
        return render(request, 'medical/addMedicine.html', context)


@login_required
def editMedicine(request, pk=None):
    """ A view to display the add medicine page """
    editMedicine = get_object_or_404(hiveMedical, pk=pk)
    if request.method == 'POST':
        form = addHiveMedicineForm(request.POST, instance=editMedicine)
        if form.is_valid():
            editMedicine = form.save(commit=False)
            editMedicine.medicine_updated = timezone.now()
            editMedicine.save()
            messages.success(
                request, f"You have successfully updated\
                     {editMedicine.medicine_name} purchased from\
                          {editMedicine.supplier_full_name} on the\
                               {editMedicine.medicine_purchase_date}",
            )
            return redirect('beeMedical')
        else:
            messages.error(request, 'Your medicine form was not valid')
    else:
        form = addHiveMedicineForm(instance=editMedicine)
        context = {
            'form': form,
        }
        return render(request, 'medical/editMedicine.html', context)


@login_required
def deleteMedicine(request, pk):
    """ A view to delete Medicine """
    datetoday = date.today()
    medicineDel = get_object_or_404(hiveMedical, pk=pk)
    if request.method == 'POST':
        messages.warning(request, f'You Have Deleted\
                         {medicineDel.medicine_name}')
        medicineDel.delete()
        return redirect('beeMedical')
    context = {
        'medicineDel': medicineDel,
        'datetoday': datetoday,
    }
    return render(request, 'medical/confirm_delete_medicine.html', context)


@login_required
def hiveMedicalHistory(request, apiaryPK, pk):
    hiveinst = get_object_or_404(hive_details, pk=pk)
    medications = hiveMedicalRecords.objects.filter(hivenumber=hiveinst.pk)
    context = {
        'medications': medications,
        'hiveinst': hiveinst,
        'apiaryPK': apiaryPK,
    }
    return render(request, 'medical/hiveMedicalHistory.html', context)


@login_required
def addMedicalRecord(request, apiaryID, pk=None):
    """ A view to display the add medicine page """
    apiary = get_object_or_404(Apiary_details, pk=apiaryID)
    user = request.user
    isMedicinePresent = hiveMedical.objects.filter(user=user)
    hiveinst = get_object_or_404(hive_details, pk=pk)
    if request.method == 'POST':
        form = addHiveMedicalRecordForm(user, request.POST)
        if form.is_valid():
            hiveMedicalRecords = form.save(commit=False)
            mednamesplit = hiveMedicalRecords.medicine_name.split(',', 4)
            getidstring = mednamesplit[3]
            splitidstring = str(getidstring)
            medid = splitidstring.split()
            hiveMedicalRecords.medicine_id = medid[1]
            hiveMedicalRecords.user = user.id
            hiveMedicalRecords.hivenumber = hiveinst
            hiveMedicalRecords.hive_name = hiveinst.hive_name
            hiveMedicalRecords.apiary_name = apiary.full_name
            hiveMedicalRecords.save()
            messages.success(
                request, f"You have successfully added a medical record to\
                    hive: {hiveinst.hive_name}",
            )
            return redirect('hiveMedicalHistory', apiaryID, pk)
        else:
            messages.error(request, 'Your medical record was not valid')
    else:
        form = addHiveMedicalRecordForm(user)
        context = {
            'form': form,
            'hiveinst': hiveinst,
            'isMedicinePresent': isMedicinePresent,
            'apiaryID': apiaryID,
        }
        return render(request, 'medical/addMedicalRecord.html', context)


@login_required
def editMedicalRecord(request, apiaryID, hiveinst_id, pk=None):
    """ A view to display the add medicine page """
    user = request.user
    hiveinst = get_object_or_404(hive_details, pk=hiveinst_id)
    editMedicineRecord = get_object_or_404(hiveMedicalRecords, pk=pk)
    if request.method == 'POST':
        form = addHiveMedicalRecordForm(user, request.POST,
                                        instance=editMedicineRecord)
        if form.is_valid():
            editMedicineRecord = form.save(commit=False)
            mednamesplit = editMedicineRecord.medicine_name.split(',', 4)
            getidstring = mednamesplit[3]
            splitidstring = str(getidstring)
            medid = splitidstring.split()
            editMedicineRecord.medicine_id = medid[1]
            editMedicineRecord.medicine_updated = timezone.now()
            editMedicineRecord.save()
            messages.success(
                request, f"You haver successfully edited a medical record for\
                    hive: {hiveinst.hive_name}",
            )
            return redirect('hiveMedicalHistory', apiaryID, hiveinst_id)
        else:
            messages.error(request, 'Your medical record was not valid')
    else:
        form = addHiveMedicalRecordForm(user, instance=editMedicineRecord)
        context = {
            'form': form,
            'hiveinst': hiveinst,
            'apiaryID': apiaryID,
        }
        return render(request, 'medical/editMedicalRecord.html', context)


@login_required
def deleteMedicalRecord(request, apiaryPK, hiveinst_id, pk):
    """ A view to delete Medicine """
    hiveid = hiveinst_id
    hiveinst = get_object_or_404(hive_details, pk=hiveid)
    recordDel = get_object_or_404(hiveMedicalRecords, pk=pk)
    if request.method == "POST":
        messages.warning(request, f'You Have Deleted The Medical Record\
                     Number:{hiveinst.hive_name}')
        recordDel.delete()
        return redirect('hiveMedicalHistory', apiaryPK, hiveinst_id)
    messages.warning(
                request, f"You are about to DELETE a medical record for\
                    hive: {hiveinst.hive_name}")
    context = {
        'recordDel': recordDel,
        'hiveid': hiveid,
        'apiaryPK': apiaryPK,
    }
    return render(request, 'medical/confirm_delete_medical_doc.html', context)
