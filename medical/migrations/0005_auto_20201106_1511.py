# Generated by Django 3.1.3 on 2020-11-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0004_hivemedical_medicine_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hivemedicalrecords',
            name='medicine_name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
