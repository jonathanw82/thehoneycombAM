from django.db import models
from apiary.models import Apiary_details
from django.contrib.auth.models import User


class hive_details(models.Model):
    UNKNOWN = 'Unknown'
    NATIONAL = 'National'
    COMMERCIAL = 'Commercial'
    NUCPOLY = '6 Frame Poly NUC'
    NUCWOOD = '6 Frame Wooden NUC'

    HIVETYPE = [(NATIONAL, 'National'),
                (COMMERCIAL, 'Commercial'),
                (NUCPOLY, '6 Frame Poly NUC'),
                (NUCWOOD, '6 Frame Wooden NUC')
                ]

    apiary_id = models.ForeignKey(Apiary_details, on_delete=models.CASCADE,
                                  default=-1)
    user = models.CharField(User, max_length=50, null=False,
                            blank=False)
    hive_name = models.CharField(max_length=50, null=False,
                                 blank=False)
    hive_type = models.CharField(choices=HIVETYPE, max_length=50,
                                 default=UNKNOWN)

    def __str__(self):
        return self.hive

    class Meta:
        verbose_name_plural = 'Hive Details'
