from django.test import TestCase
from .forms import AddApiaryForm


class TestApiaryForm(TestCase):
    def test_apiary_name_is_required(self):
        form = AddApiaryForm({"full_name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("full_name", form.errors.keys())
        self.assertEqual(form.errors["full_name"][0],
                         "This field is required.")

    def test_apiary_address1_is_required(self):
        form = AddApiaryForm({"street_address1": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("street_address1", form.errors.keys())
        self.assertEqual(form.errors["street_address1"][0],
                         "This field is required.")

    def test_apiary_address2_is_required(self):
        form = AddApiaryForm({"street_address2": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("street_address2", form.errors.keys())
        self.assertEqual(form.errors["street_address2"][0],
                         "This field is required.")

    def test_apiary_town_or_city_is_required(self):
        form = AddApiaryForm({"town_or_city": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("town_or_city", form.errors.keys())
        self.assertEqual(form.errors["town_or_city"][0],
                         "This field is required.")

    def test_apiary_county_is_required(self):
        form = AddApiaryForm({"county": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("county", form.errors.keys())
        self.assertEqual(form.errors["county"][0],
                         "This field is required.")

    def test_apiary_postcode_is_required(self):
        form = AddApiaryForm({"postcode": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("postcode", form.errors.keys())
        self.assertEqual(form.errors["postcode"][0],
                         "This field is required.")

    def test_fields_are_explicit_in_form_metaclass(self):
        form = AddApiaryForm()
        self.assertEqual(form.Meta.fields, ['full_name', 'street_address1',
                         'street_address2', 'town_or_city', 'county',
                                            'postcode'])
