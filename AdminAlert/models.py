from distutils.command.upload import upload
from hashlib import blake2b
from django.db import models

# Create your models here.
class AdminAlerts(models.Model):
    Alert_Image=models.ImageField(upload_to="Alerts/%Y/%M",null=True,blank=True)
    Alert_Message=models.CharField(max_length=255,blank=False,null=True)