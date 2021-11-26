from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Challan
# Register your models here.


@admin.register(Challan)
class ChallanAdmin(admin.ModelAdmin):
    list_display = ['challan_no', "vehicle_number", "vehicle_type", "challan_amount",
                    "challan_time", "challan_location", "challan_status"]
    list_editable = ['challan_status']
