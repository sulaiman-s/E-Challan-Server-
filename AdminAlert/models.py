from distutils.command.upload import upload
from hashlib import blake2b
from django.db import models

# Create your models here.
class AlertImage(models.Model):
    Alert_Image=models.ImageField(upload_to="Alerts/%Y/%M",null=True,blank=False)
    def __str__(self) -> str:
        return "Alert Image"

class AlertMessage(models.Model):
    Alert_Message=models.CharField(max_length=255,blank=False,null=True)
    def __str__(self) -> str:
        return self.Alert_Message
