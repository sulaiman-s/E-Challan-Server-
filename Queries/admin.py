from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Queries)
class QuereyAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "mesage"]


@admin.register(models.Uploads)
class UploadAdmin(admin.ModelAdmin):
    list_display = ["vehicle_number", "challan_image"]
    list_editable = ["challan_image"]
