from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from hives.models import hive_details


# Create your models here.


class hiveMedical(models.Model):
    """
    A Model for Hive Medical Medicine
    """
    user = models.CharField(User, max_length=50, null=False,
                            blank=False)
    supplier_full_name = models.CharField(max_length=50, null=False,
                                          blank=False)
    supplier_street_address1 = models.CharField(max_length=80, null=False,
                                                blank=False)
    supplier_street_address2 = models.CharField(max_length=80, null=False,
                                                blank=False)
    supplier_town_or_city = models.CharField(max_length=40, null=False,
                                             blank=False)
    supplier_county = models.CharField(max_length=80, null=False,
                                       blank=False)
    supplier_postcode = models.CharField(max_length=20, null=False,
                                         blank=False)
    medicine_name = models.CharField(max_length=80, null=False,
                                     blank=False)
    medicine_purchase_date = models.DateField(null=True, blank=True)
    medicine_batch_number = models.CharField(max_length=80, null=False,
                                             blank=False)
    medicine_qty = models.CharField(max_length=80, null=False,
                                    blank=False)
    medicine_exp_date = models.DateField(null=True, blank=True)
    medicine_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.hiveMedical

    class Meta:
        verbose_name_plural = 'Hive Medical Medicine'


class hiveMedicalRecords(models.Model):
    """
    A Model for Hive Medical Medicine
    """

    hivenumber = models.ForeignKey(hive_details, on_delete=models.CASCADE,
                                   default=-1)
    hive_name = models.CharField(max_length=50, null=False,
                                 blank=False)
    medicine_name = models.CharField(max_length=80, blank=True, null=True)
    medicine_admin_time_and_date = models.DateTimeField(blank=True, null=True,
                                                        default=timezone.now)
    medicine_updated = models.DateTimeField(blank=True, null=True)
    medicine_duration = models.CharField(max_length=20, null=False,
                                         blank=False)
    medicine_withdrawal = models.CharField(max_length=50, null=True,
                                           blank=True)
    medicine_qty_used = models.CharField(max_length=20, null=False,
                                         blank=False)
    deployment_method = models.CharField(max_length=50, null=True, blank=True)
    medicine_disposal = models.CharField(max_length=150, null=False,
                                         blank=False)
    medicine_disposal_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.hiveMedicalRecords

    class Meta:
        verbose_name_plural = 'Hive Medical Records'
