from django.db import models

# Create your models here.


class Queries(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mesage = models.TextField(max_length=300)

    def __str__(self) -> str:
        return self.name


class Uploads(models.Model):
    vehicle_number = models.CharField(max_length=100)
    challan_image = models.ImageField(upload_to="uploaded/%Y/%m", blank=False)

    def __str__(self) -> str:
        return self.vehicle_number


class MLImages(models.Model):
    ml_image = models.ImageField(upload_to="mlImages/%Y/%m", blank=False)
