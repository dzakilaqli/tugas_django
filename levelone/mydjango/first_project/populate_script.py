import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import VehicleType, Vehicle, OwnershipRecord
from faker import Faker
from datetime import datetime


django.setup()

# Inisialisasi Faker
fake = Faker()

# Data kendaraan contoh
vehicle_types = ['Car', 'Motorcycle', 'Truck', 'Bus']

def add_vehicle_type():
    for vt in vehicle_types:
        VehicleType.objects.get_or_create(type_name=vt)

def populate(n=5):
    add_vehicle_type()

    for _ in range(n):
        vehicle_type = VehicleType.objects.order_by('?').first()

        # Data palsu
        owner_name = fake.name()
        license_plate = fake.license_plate()[:15]
        color = fake.color_name()
        vin = fake.bothify(text="??#########???????")  # VIN format contoh

        
        vehicle, created = Vehicle.objects.get_or_create(
            vehicle_type=vehicle_type,
            owner_name=owner_name,
            license_plate=license_plate,
            color=color,
            vin=vin
        )

       
        purchase_date = fake.date_this_decade(before_today=True, after_today=False)
        OwnershipRecord.objects.get_or_create(vehicle=vehicle, purchase_date=purchase_date)

if __name__ == '__main__':
    print("Mengisi data dummy...")
    populate(20) 
    print("Selesai!")
