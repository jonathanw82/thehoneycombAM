from django import forms
from .models import hiveMedical, hiveMedicalRecords


class DateInput(forms.DateInput):
    """
    This function creates a widget to make
    a Date Input field.
    """
    input_type = 'date'


class addHiveMedicineForm(forms.ModelForm):

    class Meta:
        widgets = {'medicine_exp_date': DateInput(),
                   'medicine_purchase_date': DateInput()}
        model = hiveMedical
        fields = [
            'medicine_name',
            'supplier_full_name',
            'supplier_street_address1',
            'supplier_street_address2',
            'supplier_town_or_city',
            'supplier_county',
            'supplier_postcode',
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
        widgets = {'medicine_disposal_date': DateInput()}

        model = hiveMedicalRecords
        fields = [
            'medicine_name',
            'medicine_duration',
            'medicine_withdrawal',
            'medicine_qty_used',
            'deployment_method',
            'medicine_disposal',
            'medicine_disposal_date']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        choices = [(med.medicine_name + ', ' +
                    ' Batch Num: ' +
                    med.medicine_batch_number + ', ' +
                    ' Exp: ' +
                    str(med.medicine_exp_date) + ', ' +
                    'ID: ' + str(med.pk),
                    med.medicine_name + ', ' +
                    ' Batch Num: ' +
                    med.medicine_batch_number + ', ' +
                    ' Exp: ' +
                    str(med.medicine_exp_date) + ', ' +
                    'ID: ' + str(med.pk))
                   for med in hiveMedical.objects.filter(user=user)]

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-hive-form'
            self.fields['medicine_name'] = forms.ChoiceField(
                                widget=forms.Select(), choices=choices)
