# Generated by Django 3.1.3 on 2020-12-01 09:37

from django.db import migrations, models
import hives.models


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0008_auto_20201130_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hivedocuments',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=hives.models.hiveDocuments.get_file_path),
        ),
        migrations.AlterField(
            model_name='hivedocuments',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=hives.models.hiveDocuments.get_file_path),
        ),
    ]
