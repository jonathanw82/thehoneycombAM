# Generated by Django 3.1.3 on 2020-11-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0002_auto_20201109_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hivedocuments',
            name='weather',
            field=models.CharField(choices=[('Over Cast', 'Over Cast'), ('Sunny', 'Sunny'), ('Sunny & HOT', 'Sunny & HOT'), ('Fair', 'Fair'), ('Raining', 'Rain'), ('Thundery', 'Thundery'), ('Snow', 'Snow'), ('Fog', 'Fog')], default='Fair', max_length=20),
        ),
    ]