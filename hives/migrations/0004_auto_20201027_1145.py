# Generated by Django 3.1.1 on 2020-10-27 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0003_auto_20201027_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hive_details',
            old_name='apiary_id',
            new_name='apiary',
        ),
    ]
