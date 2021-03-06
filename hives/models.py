from django.db import models
from apiary.models import Apiary_details
from django.contrib.auth.models import User
import uuid
import os


class hive_details(models.Model):
    UNKNOWN = 'Unknown'
    APIDEA = 'Apidea'
    NATIONAL = 'National'
    NATIONALPOLLY = 'National Polly'
    NATLARGE = '14x12 National'
    NATLARGEPOLLY = '14x12 National Polly'
    COMMERCIAL = 'Commercial'
    COMMERCIALPOLLY = 'Commercial Polly'
    NUCPOLY = '6 Frame Poly NUC'
    NUCWOOD = '6 Frame Wooden NUC'
    WBC = 'WBC'
    CDB = 'CDB'
    LANGSTROTH = 'Langstroth'
    LANGSTROTHPOLLY = 'Langstroth Polly'
    SMITH = 'Smith'
    TOPB = 'Top Bar'
    SK = 'Skep'
    DAN = 'Dadant'
    FLOW = 'Flow'
    WAR = 'Warré'
    ROSE = 'Rose'
    DLD = 'Dartington Long Deep'
    BEEHAUS = 'Beehaus'
    LB = 'Long Box Hive'

    HIVETYPE = [(NATIONAL, 'BS National'),
                (NATIONALPOLLY, 'BS National Polly'),
                (NATLARGE, '14x12 National'),
                (NATLARGEPOLLY, '14x12 National Polly'),
                (COMMERCIAL, 'BS Commercial'),
                (COMMERCIALPOLLY, 'BS Commercial Polly'),
                (NUCPOLY, '6 Frame Poly NUC'),
                (NUCWOOD, '6 Frame Wooden NUC'),
                (APIDEA, 'Apidea'),
                (WBC, 'WBC'),
                (CDB, 'CDB'),
                (LANGSTROTH, 'Langstroth'),
                (LANGSTROTHPOLLY, 'Langstroth Polly'),
                (SMITH, 'Smith'),
                (TOPB, 'Top Bar'),
                (SK, 'Skep'),
                (DAN, 'Dadant'),
                (FLOW, 'Flow'),
                (WAR, 'Warré'),
                (ROSE, 'Rose'),
                (DLD, 'Dartington Long Deep'),
                (BEEHAUS, 'Beehaus'),
                (LB, 'Long Box')
                ]

    apiary_id = models.ForeignKey(Apiary_details, on_delete=models.CASCADE,
                                  null=True, blank=True)
    user = models.CharField(User, max_length=50, null=False,
                            blank=False)
    hive_name = models.CharField(max_length=50, null=False,
                                 blank=False)
    hive_type = models.CharField(choices=HIVETYPE, max_length=50,
                                 default=UNKNOWN)
    old_hive_type = models.CharField(max_length=50, null=True,
                                     blank=True)
    hive_new_apiary = models.CharField(max_length=50, null=True,
                                       blank=True)
    hive_old_apiary = models.CharField(max_length=50, null=True,
                                       blank=True)
    hive_move_date = models.DateField(null=True, blank=True)
    hive_old_name = models.CharField(max_length=50, null=True,
                                     blank=True)
    been_merged = models.CharField(max_length=10, null=True,
                                   blank=True)                               

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

    # NOTMERGED = 'Not Merged'

    def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('media/images/', filename)
    user = models.CharField(User, max_length=50, null=False,
                            blank=False)
    hivenumber = models.ForeignKey(hive_details, on_delete=models.CASCADE,
                                   null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    queen = models.BooleanField(default=False)
    queenColour = models.CharField(choices=QUEENCOL, max_length=50,
                                   default=NOTYETRECORD)
    qcnum = models.IntegerField(blank=True, null=True, default=0)
    eggs = models.IntegerField(blank=True, null=True, default=0)
    brood = models.IntegerField(blank=True, null=True, default=0)
    food = models.IntegerField(blank=True, null=True, default=0)
    supersnum = models.IntegerField(blank=True, null=True, default=0)
    weather = models.CharField(choices=WEATHER, max_length=20,
                               default=F)
    notes = models.CharField(max_length=500, blank=True, null=True)
    temperment = models.CharField(choices=TEMPER, max_length=20,
                                  default=A)
    beekeepername = models.CharField(max_length=30, blank=True, null=True)
    merged_with = models.CharField(max_length=30, blank=True, null=True)
    merged_date = models.DateField(null=True, blank=True)
    image1 = models.ImageField(upload_to=get_file_path,
                               blank=True, null=True)
    image2 = models.ImageField(upload_to=get_file_path,
                               blank=True, null=True)

    def __str__(self):
        return self.hiveDocuments

    class Meta:
        verbose_name_plural = 'Hive Documents'
