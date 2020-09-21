from django import forms
from .models import Apiary_details


class AddApiaryForm(forms.ModelForm):

    class Meta:
        model = Apiary_details
        fields = ['full_name', 'street_address1', 'street_address2',
                  'town_or_city', 'county', 'postcode']

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-apiary-form'
