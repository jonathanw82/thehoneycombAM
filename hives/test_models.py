from django.test import TestCase
from .models import hive_details
from apiary.models import Apiary_details


class TestHiveModels(TestCase):

    # def test_apiary_id_string_method_returns_name(self):
    #     apiary = Apiary_details.objects.create(full_name='test')
    #     item = hive_details.objects.create(f'apiary_id='{apiary.id}')
    #     self.assertEqual(str(item), 'Test Todo Item')

    def test_hive_name_string_method_returns_name(self):
        item = hive_details.objects.create(hive_name='Test')
        self.assertEqual(str(item), 'Test')

    # def test_hive_type_string_method_returns_name(self):
    #     item = hive_details.objects.create(hive_type='Test')
    #     self.assertEqual(str(item), 'Test')

    # def test_hive_new_apiary_string_method_returns_name(self):
    #     item = hive_details.objects.create(hive_new_apiary='Test')
    #     self.assertEqual(str(item), 'Test')

    # def test_hive_old_apiary_string_method_returns_name(self):
    #     item = hive_details.objects.create(hive_old_apiary='Test')
    #     self.assertEqual(str(item), 'Test')
