from django import forms
from .models import hive_details


class AddHiveForm(forms.ModelForm):

    class Meta:
        model = hive_details
        fields = ['hive_name']

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-hive-form'
