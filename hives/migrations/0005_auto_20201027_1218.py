# Generated by Django 3.1.1 on 2020-10-27 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0004_auto_20201027_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hive_details',
            name='apiary',
        ),
        migrations.AddField(
            model_name='hive_details',
            name='apiary_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
