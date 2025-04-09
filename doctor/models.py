from django.db import models

class Doctor(models.Model):
    doctorName = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50)
    education = models.CharField(max_length=100)
    experience = models.IntegerField()
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    available_time = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
