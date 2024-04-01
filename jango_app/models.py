from django.db import models

class CarDetails(models.Model):
    car_name = models.CharField(max_length=10,primary_key=True)
    brand_name = models.CharField(max_length=10)
    colour = models.CharField(max_length=10)
    length_width_height = models.CharField(max_length=25)
    displacement = models.CharField(max_length=10)
    power = models.CharField(max_length=30)
    torque = models.CharField(max_length=30)
    cylinder = models.CharField(max_length=2)
    gear = models.CharField(max_length=10)
    ground_clearance = models.CharField(max_length=10)
    car_type = models.CharField(max_length=10)
    engine = models.CharField(max_length=10)
    fuel_tank = models.CharField(max_length=10)
    prize = models.CharField(max_length=10)

class Registration(models.Model):
    Name = models.CharField(max_length=20)
    Gender = models.CharField(max_length=10)
    Date_of_birth = models.CharField(max_length=14)
    Phone = models.CharField(max_length=10)
    Email = models.CharField(max_length=50 ,primary_key=True)
    Address = models.CharField(max_length=100)
    Password = models.CharField(max_length=20)

    



