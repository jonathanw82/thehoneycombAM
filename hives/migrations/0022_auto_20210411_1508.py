# Generated by Django 3.1.3 on 2021-04-11 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0021_auto_20210411_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hivedocuments',
            name='merged_with',
            field=models.CharField(blank=True, default='Not Merged', max_length=50, null=True),
        ),
    ]