from django.contrib import admin
from .models import hive_details, hiveDocuments


class hiveAdmin(admin.ModelAdmin):
    list_display = (
        'hive_name',
        'hive_type',
        'user',
    )


class hivedocumentsAdmin(admin.ModelAdmin):

    list_display = (
        'date',
        'queen',
        'queenColour',
        'qcnum',
        'eggs',
        'brood',
        'supersnum',
        'weather',
        'notes',
        'beekeepername',
        'image1',
        'image2'
    )


# Register your models here.
admin.site.register(hive_details, hiveAdmin)
admin.site.register(hiveDocuments, hivedocumentsAdmin)
