from django.db import models
from apiary.models import Apiary_details
from django.contrib.auth.models import User


class hive_details(models.Model):

    apiary_id = models.CharField(max_length=50, null=False,
                                 blank=False)
    user = models.CharField(User, max_length=50, null=False,
                            blank=False)
    hive_name = models.CharField(max_length=50, null=False,
                                 blank=False)

    def __str__(self):
        return self.hive

    class Meta:
        verbose_name_plural = 'Hive Details'
