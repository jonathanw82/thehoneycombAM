# Generated by Django 3.1.3 on 2020-11-05 14:36

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hives', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hiveMedical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, verbose_name=django.contrib.auth.models.User)),
                ('supplier_full_name', models.CharField(max_length=50)),
                ('supplier_street_address1', models.CharField(max_length=80)),
                ('supplier_street_address2', models.CharField(max_length=80)),
                ('supplier_town_or_city', models.CharField(max_length=40)),
                ('supplier_county', models.CharField(max_length=80)),
                ('supplier_postcode', models.CharField(max_length=20)),
                ('medicine_name', models.CharField(max_length=80)),
                ('medicine_purchase_date', models.DateField(blank=True, null=True)),
                ('medicine_batch_number', models.CharField(max_length=80)),
                ('medicine_qty', models.CharField(max_length=80)),
                ('medicine_exp_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Hive Medical Medicine',
            },
        ),
        migrations.CreateModel(
            name='hiveMedicalRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hive_name', models.CharField(max_length=50)),
                ('medicine_name', models.CharField(max_length=80)),
                ('medicine_admin_time_and_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('medicine_duration', models.CharField(max_length=20)),
                ('medicine_withdrawal', models.CharField(blank=True, max_length=50, null=True)),
                ('medicine_qty_used', models.CharField(max_length=20)),
                ('medicine_disposal', models.CharField(max_length=150)),
                ('medicine_disposal_date', models.DateField(blank=True, null=True)),
                ('hivenumber', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='hives.hive_details')),
            ],
            options={
                'verbose_name_plural': 'Hive Medical Records',
            },
        ),
    ]