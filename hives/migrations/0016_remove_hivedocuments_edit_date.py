# Generated by Django 3.1.3 on 2021-03-31 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0015_hivedocuments_edit_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hivedocuments',
            name='edit_date',
        ),
    ]