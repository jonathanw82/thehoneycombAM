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
