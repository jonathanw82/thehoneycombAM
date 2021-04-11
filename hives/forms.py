from django import forms
from .widgets import CustomClearableFileInput
from .models import hive_details, Apiary_details, hiveDocuments


class DateInput(forms.DateInput):
    """
    This function creates a widget to make
    a Date Input field.
    """
    input_type = 'date'


class AddHiveForm(forms.ModelForm):

    class Meta:
        model = hive_details
        fields = ['hive_name', 'hive_type']

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-hive-form'
            self.fields['hive_name'].label = 'Name or Number'


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
        widgets = {'edit_date': DateInput(), 'merged_date': DateInput()}
        model = hiveDocuments
        fields = ['queen', 'queenColour',
                  'qcnum', 'eggs', 'brood',
                  'food',
                  'supersnum', 'weather',
                  'temperment',
                  'notes', 'beekeepername',
                  'merged_date', 'merged_with',
                  'image1', 'image2']

    image1 = forms.ImageField(label='Image 1', required=False,
                              widget=CustomClearableFileInput)
    image2 = forms.ImageField(label='Image 2', required=False,
                              widget=CustomClearableFileInput)

    def __init__(self, userID, *args, **kwargs):
        super().__init__(*args, **kwargs)

        initialChoice = [('', 'Select:')]
        choices = [(hive.hive_name, hive.hive_name.capitalize())
                   for hive in hive_details.objects.filter(user=userID)]

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'add-hive-form'
            self.fields['qcnum'].label = 'Queen cells?'
            self.fields['eggs'].label = 'Eggs? on how many frames'
            self.fields['brood'].label = 'Brood Capped? on how many frames'
            self.fields['food'].label = 'Food? on how many frames'
            self.fields['merged_date'].label = 'If merged when was it merged'
            self.fields['merged_with'] = forms.ChoiceField(required=False,
                                                           label='Merged with what hive?', 
                                                           widget=forms.Select(),
                                                           choices=initialChoice + choices)
