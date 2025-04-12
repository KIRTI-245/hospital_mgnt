from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    bloodGroup = models.CharField(max_length=5)
    allergies = models.TextField()
    medication = models.TextField()
    surgeries = models.TextField()
    notes = models.TextField()
    doctorAssigned = models.ForeignKey('doctor.Doctor', on_delete=models.CASCADE)


