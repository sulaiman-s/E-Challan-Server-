from django.contrib import admin
from . import models
from django.utils.html import format_html
# Register your models here.


@admin.register(models.Queries)
class QuereyAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "mesage"]


@admin.register(models.Uploads)
class UploadAdmin(admin.ModelAdmin):
    list_display = ["vehicle_number", "Reciept_Image"]
    search_fields = ["vehicle_number", "Reciept_Image"]

    def Reciept_Image(self, obj):
        return format_html('<img src="{}" style="width: 100px; height:100px;" />'.format(obj.challan_image.url))
    Reciept_Image.allow_tags = True


@admin.register(models.MLImages)
class MLAdmin(admin.ModelAdmin):
    list_display = ["Ml_image"]

    def Ml_image(self, obj):
        return format_html('<img src="{}" style="width: 100px; height:100px;" />'.format(obj.ml_image.url))
    Ml_image.allow_tags = True
