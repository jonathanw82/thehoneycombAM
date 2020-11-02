from django import forms
from .models import hive_details, Apiary_details, hiveDocuments


class AddHiveForm(forms.ModelForm):

    class Meta:
        model = hive_details
        fields = ['hive_name', 'hive_type']

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-hive-form'


class editHiveForm(forms.ModelForm):

    class Meta:
        model = hive_details
        fields = ['hive_name', 'hive_type',
                  'apiary_id']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-hive-form'
            self.fields['apiary_id'].label = 'Move Hive To:'
            # filter the queryset to only display the elements that belong to
            # the current logged in user/owner by dringing in the
            # user to the __init__
            self.fields['apiary_id'].queryset = Apiary_details.objects.filter(
                user=user)


class addHiveDocumentsForm(forms.ModelForm):

    class Meta:
        model = hiveDocuments
        fields = ['queen', 'queenColour', 'qc',
                  'qcnum', 'eggs',
                  'supers', 'supersnum',
                  'weather', 'notes', 'beekeepername',
                  'image1', 'image2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-hive-form'
