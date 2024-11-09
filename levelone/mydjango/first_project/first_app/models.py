from django.db import models

# Create your models here.

class VehicleType(models.Model):
    type_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.type_name


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=264)
    license_plate = models.CharField(max_length=15, unique=True)
    color = models.CharField(max_length=50)
    vin = models.CharField(max_length=17, unique=True)  # VIN typically 17 characters long

    def __str__(self):
        return f"{self.license_plate} - {self.owner_name}"


class OwnershipRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    purchase_date = models.DateField()

    def __str__(self):
        return f"{self.vehicle} - {self.purchase_date}"