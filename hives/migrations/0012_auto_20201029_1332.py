# Generated by Django 3.1.1 on 2020-10-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0011_auto_20201029_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hivedocuments',
            name='qcnum',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hivedocuments',
            name='supersnum',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
