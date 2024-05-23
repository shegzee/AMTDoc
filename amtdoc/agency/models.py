from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
	(0, 'male'),
	(1, 'female'),
)

class User(AbstractUser):
	pass

class Lga(models.Model):
	name = models.CharField(max_length=255)

class Agent(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	lga = models.ForeignKey(Lga, on_delete=models.CASCADE)
	town = models.CharField(max_length=255)
	phone = models.CharField(max_length=20)

class Patient(models.Model):
	agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
	gender = models.IntegerField(choices=GENDER_CHOICES)
	dob = models.DateField()
	phone = models.CharField(max_length=20, blank=True, null=True)
	address = models.TextField()

class Doctor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	name = models.CharField(max_length=255)
