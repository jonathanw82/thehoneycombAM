# Generated by Django 3.1.1 on 2020-10-27 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiary', '0001_initial'),
        ('hives', '0006_auto_20201027_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hive_details',
            name='apiary_id',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='apiary.apiary_details'),
        ),
    ]
