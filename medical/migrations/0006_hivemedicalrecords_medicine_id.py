# Generated by Django 3.1.3 on 2020-12-16 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0005_auto_20201106_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='hivemedicalrecords',
            name='medicine_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
