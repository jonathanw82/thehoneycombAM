from django.test import TestCase
from .forms import AddHiveForm
from .forms import addHiveDocumentsForm


class TestAddHiveForm(TestCase):

    def test_hive_name_is_required(self):
        form = AddHiveForm({"hive_name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("hive_name", form.errors.keys())
        self.assertEqual(form.errors["hive_name"][0],
                         "This field is required.")

    def test_hive_type_is_required(self):
        form = AddHiveForm({"hive_type": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("hive_type", form.errors.keys())
        self.assertEqual(form.errors["hive_type"][0],
                         "This field is required.")

    def test_fields_are_explicit_in_form_metaclass(self):
        form = AddHiveForm()
        self.assertEqual(form.Meta.fields, ['hive_name', 'hive_type'])


class TestAddHiveDocForm(TestCase):

    def test_queen_is_not_required(self):
        form = addHiveDocumentsForm({"Queen": "Test Hive"})
        self.assertFalse(form.is_valid())

    def test_queenColor_is_required(self):
        form = addHiveDocumentsForm({"QueenColor": ""})
        self.assertFalse(form.is_valid())

    def test_qc_is_not_required(self):
        form = addHiveDocumentsForm({"Qc": "Test Hive"})
        self.assertFalse(form.is_valid())

    def test_qc_num_not_required(self):
        form = addHiveDocumentsForm({"qcnum": "Test Hive"})
        self.assertFalse(form.is_valid())

    def test_eggs_not_required(self):
        form = addHiveDocumentsForm({"eggs": "Test Hive"})
        self.assertFalse(form.is_valid())

    def test_brood_not_required(self):
        form = addHiveDocumentsForm({"brood": "Test Hive"})
        self.assertFalse(form.is_valid())

    def test_supers_not_required(self):
        form = addHiveDocumentsForm({"supers": "Test Hive"})
        self.assertFalse(form.is_valid())

    def test_supers_num_not_required(self):
        form = addHiveDocumentsForm({"supersnum": "Test Hive"})
        self.assertFalse(form.is_valid())

    def test_weather_required(self):
        form = addHiveDocumentsForm({"weather": ""})
        self.assertFalse(form.is_valid())

    def test_temperment_required(self):
        form = addHiveDocumentsForm({"temperment": ""})
        self.assertFalse(form.is_valid())

    def test_notes_not_required(self):
        form = addHiveDocumentsForm({"notes": "Test Queen Cell"})
        self.assertFalse(form.is_valid())

    def test_beekeepersname_not_required(self):
        form = addHiveDocumentsForm({"beekeesname": "Test Queen Cell"})
        self.assertFalse(form.is_valid())

    def test_image1_not_required(self):
        form = addHiveDocumentsForm({"image1": "Test Queen Cell"})
        self.assertFalse(form.is_valid())

    def test_image2_not_required(self):
        form = addHiveDocumentsForm({"image2": "Test Queen Cell"})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = addHiveDocumentsForm()
        self.assertEqual(form.Meta.fields, ['queen', 'queenColour', 'qc',
                                            'qcnum', 'eggs', 'brood',
                                            'supersnum', 'weather',
                                            'temperment',
                                            'notes', 'beekeepername',
                                            'image1', 'image2'])
