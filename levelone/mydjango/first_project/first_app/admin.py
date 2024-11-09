from django.contrib import admin
from .models import VehicleType, Vehicle, OwnershipRecord

# Register your models here.
admin.site.register(VehicleType)
admin.site.register(Vehicle)
admin.site.register(OwnershipRecord)
