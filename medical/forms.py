from django import forms
from .models import hiveMedical, hiveMedicalRecords


class addHiveMedicineForm(forms.ModelForm):

    class Meta:
        model = hiveMedical
        fields = [
            'supplier_full_name',
            'supplier_street_address1',
            'supplier_street_address2',
            'supplier_town_or_city',
            'supplier_county',
            'supplier_postcode',
            'medicine_name',
            'medicine_purchase_date',
            'medicine_batch_number',
            'medicine_qty',
            'medicine_exp_date',
           ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-hive-form'


class addHiveMedicalRecordForm(forms.ModelForm):

    class Meta:
        model = hiveMedicalRecords
        fields = [
            'medicine_admin_time_and_date',
            'medicine_duration',
            'medicine_withdrawal',
            'medicine_qty_used',
            'medicine_disposal',
            'medicine_disposal_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-hive-form'