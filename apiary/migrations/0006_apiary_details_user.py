# Generated by Django 3.1.1 on 2020-09-18 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apiary', '0005_remove_apiary_details_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiary_details',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
