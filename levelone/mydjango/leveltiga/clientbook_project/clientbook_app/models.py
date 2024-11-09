from django.db import models

# Create your models here.
class Pelanggan(models.Model):
    nama_depan = models.CharField(max_length=100)
    nama_belakang = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)