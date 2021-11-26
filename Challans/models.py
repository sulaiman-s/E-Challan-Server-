from django.db import models

# Create your models here.


class Challan(models.Model):
    challan_choices = [("Bi", "Bike"), ("Ca", "Car"),
                       ("Tr", "Truck"), ("Bu", "Bus")]
    status_choices = [("P", "Paid"), ("NP", "Not Paid")]
    challan_no = models.CharField(primary_key=True, max_length=255)
    vehicle_number = models.CharField(unique=True, max_length=255)
    vehicle_type = models.CharField(
        choices=challan_choices, default="Bike", max_length=255)
    challan_amount = models.CharField(max_length=255)
    challan_time = models.DateTimeField(auto_now=True)
    challan_location = models.TextField()
    challan_status = models.CharField(choices=status_choices, max_length=255)

    def __str__(self) -> str:
        return self.challan_no, self.vehicle_number
