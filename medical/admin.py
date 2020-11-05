from django.contrib import admin
from .models import hiveMedical, hiveMedicalRecords

# Register your models here.


class hiveMedicalAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'supplier_full_name',
        'supplier_street_address1',
        'supplier_street_address2',
        'supplier_town_or_city',
        'supplier_county',
        'supplier_postcode',
        'medicine_name',
        'medicine_purchase_date',
        'medicine_batch_number',
        'medicine_qty',
        'medicine_exp_date',
    )


class hiveMedicalRecordsAdmin(admin.ModelAdmin):

    list_display = [
        'hivenumber',
        'hive_name',
        'medicine_name',
        'medicine_admin_time_and_date',
        'medicine_duration',
        'medicine_withdrawal',
        'medicine_qty_used',
        'medicine_disposal',
        'medicine_disposal_date'
    ]


admin.site.register(hiveMedical, hiveMedicalAdmin)
admin.site.register(hiveMedicalRecords, hiveMedicalRecordsAdmin)
