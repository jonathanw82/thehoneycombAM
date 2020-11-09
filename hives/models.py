from django.db import models
from apiary.models import Apiary_details
from django.contrib.auth.models import User
from django.utils import timezone


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
    hive_new_apiary = models.CharField(max_length=50, null=True,
                                       blank=True)
    hive_old_apiary = models.CharField(max_length=50, null=True,
                                       blank=True)
    hive_move_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.hive_name

    class Meta:
        verbose_name_plural = 'Hive Details'


class hiveDocuments(models.Model):
    """
    A Model for Hive Documents
    """
    WHITE = 'White'
    YELLOW = 'Yellow'
    RED = 'Red'
    GREEN = 'Green'
    BLUE = 'Blue'
    NOTYETRECORD = 'Not Marked'

    QUEENCOL = [(WHITE, 'White'),
                (YELLOW, 'Yellow'),
                (RED, 'Red'),
                (GREEN, 'Green'),
                (BLUE, 'Blue'),
                (NOTYETRECORD, 'Not Marked')
                ]

    OC = 'Over Cast'
    S = 'Sunny'
    SNH = 'Sunny & HOT'
    F = 'Fair'
    R = 'Raining'
    THUN = 'Thundery'
    SNOW = 'Snow'
    FOG = 'Fog'

    WEATHER = [(OC, 'Over Cast'),
               (S, 'Sunny'),
               (SNH, 'Sunny & HOT'),
               (F, 'Fair'),
               (R, 'Rain'),
               (THUN, 'Thundery'),
               (SNOW, 'Snow'),
               (FOG, 'Fog')]

    DE = 'Select'
    A = '5 Calm'
    B = '4'
    C = '3'
    D = '2'
    E = '1 Evil'

    TEMPER = [(A, '5 Calm'),
              (B, '4'),
              (C, '3'),
              (D, '2'),
              (E, '1 Evil')]

    hivenumber = models.ForeignKey(hive_details, on_delete=models.CASCADE,
                                   default=-1)
    date = models.DateField(null=True, blank=True)
    queen = models.BooleanField(default=False)
    queenColour = models.CharField(choices=QUEENCOL, max_length=50,
                                   default=NOTYETRECORD)
    qc = models.BooleanField(default=False)
    qcnum = models.IntegerField(blank=True, null=True)
    eggs = models.BooleanField(default=False)
    brood = models.BooleanField(default=False)
    supersnum = models.IntegerField(blank=True, null=True, default=0)
    weather = models.CharField(choices=WEATHER, max_length=20,
                               default=F)
    notes = models.CharField(max_length=500, blank=True, null=True)
    temperment = models.CharField(choices=TEMPER, max_length=20,
                                  default=A)
    beekeepername = models.CharField(max_length=30, blank=True, null=True)
    image1 = models.ImageField(upload_to='media/images/',
                               blank=True, null=True)
    image2 = models.ImageField(upload_to='media/images/',
                               blank=True, null=True)

    def __str__(self):
        return self.hiveDocuments

    class Meta:
        verbose_name_plural = 'Hive Documents'
