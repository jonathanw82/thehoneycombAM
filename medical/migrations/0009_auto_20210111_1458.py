# Generated by Django 3.1.3 on 2021-01-11 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0008_auto_20201216_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hivemedicalrecords',
            name='deployment_method',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hivemedicalrecords',
            name='medicine_disposal',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
