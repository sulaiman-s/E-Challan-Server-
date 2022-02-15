from django.contrib import admin
from django.utils.html import format_html
from AdminAlert.models import AlertImage, AlertMessage

# Register your models here.

@admin.register(AlertImage)
class AdminAlertImage(admin.ModelAdmin):
    list_display=['Alert_image']

    def Alert_image(self,obj):
        if obj.Alert_Image.url:
            return format_html('<img src="{}" style="width: 100px; height:100px;" />'.format(obj.Alert_Image.url))
        else:
            return "not set"
            
    Alert_image.allow_tags=True
    
@admin.register(AlertMessage)
class AdminAlertMessage(admin.ModelAdmin):
    list_display=['Alert_Message']