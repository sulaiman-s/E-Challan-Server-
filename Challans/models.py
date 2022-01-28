from django.db import models

# Create your models here.


class Challan(models.Model):
    challan_id=models.AutoField(primary_key=True)
    challan_choices = [("Bike", "Bike"), ("Car", "Car"),
                       ("Truck", "Truck"), ("Bus", "Bus")]
    status_choices = [("Paid", "Paid"), ("NotPaid", "Not Paid")]
    vehicle_number = models.CharField(max_length=255)
    vehicle_type = models.CharField(
        choices=challan_choices, default="Bike", max_length=255)
    challan_amount = models.CharField(max_length=255)
    challan_time = models.DateTimeField(auto_now=True)
    challan_location = models.TextField()
    challan_status = models.CharField(choices=status_choices,default="NotPaid", max_length=255)

    def __str__(self) -> str:
        return self.vehicle_number
