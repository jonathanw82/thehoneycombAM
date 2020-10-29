# Generated by Django 3.1.1 on 2020-10-29 13:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0009_auto_20201028_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='hiveDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_and_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('queen', models.BooleanField(default=False)),
                ('qc', models.BooleanField(default=False)),
                ('qcnum', models.IntegerField()),
                ('eggs', models.BooleanField(default=False)),
                ('supers', models.BooleanField(default=False)),
                ('supersnum', models.IntegerField()),
                ('weather', models.CharField(blank=True, max_length=20, null=True)),
                ('notes', models.CharField(blank=True, max_length=500, null=True)),
                ('beekeepername', models.CharField(blank=True, max_length=30, null=True)),
                ('hive', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='hives.hive_details')),
            ],
            options={
                'verbose_name_plural': 'Hive Documents',
            },
        ),
    ]
