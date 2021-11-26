from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, _ChoiceNamedGroup

# Create your models here.


class Challan(models.Model):
    challan_choices = [("Bi", "Bike"), ("Ca", "Car"),
                       ("Tr", "Truck"), ("Bu", "Bus")]
    status_choices = [("P", "Paid"), ("NP", "Not Paid")]
    challan_no = models.CharField(primary_key=True, max_length=100)
    vehicle_number = models.CharField(unique=True)
    vehicle_type = models.CharField(
        choices=challan_choices, default="Bike", max_length=1)
    challan_amount = models.CharField()
    challan_time = models.DateTimeField(auto_now=True)
    challan_location = models.TextField()
    challan_status = models.CharField(choices=status_choices)


class Queries(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mesage = models.TextField(max_length=300)


class Uploads(models.Model):
    vehicle_number = models.CharField(max_length=100)
    challan_image = models.ImageField(upload_to="uploaded/%Y/%m", blank=True)
