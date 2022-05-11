from distutils.command.upload import upload
from django.db import models

# Create your models here.


class UserHistory(models.Model):
    number = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    image = models.ImageField(upload_to="history", blank=False)
    name=models.CharField(max_length=255)


class WardenHistory(models.Model):
    number = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    name=models.CharField(max_length=255)

