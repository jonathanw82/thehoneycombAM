from django.db import models
from django.contrib.auth.models import User


class Apiary_details(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=False,
                                 blank=False)
    street_address1 = models.CharField(max_length=80, null=False,
                                       blank=False)
    street_address2 = models.CharField(max_length=80, null=False,
                                       blank=False)
    town_or_city = models.CharField(max_length=40, null=False,
                                    blank=False)
    county = models.CharField(max_length=80, null=False,
                              blank=False)
    postcode = models.CharField(max_length=20, null=False,
                                blank=False)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Apiary Details'
