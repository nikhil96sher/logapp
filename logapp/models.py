from django.db import models
from django.contrib.auth.models import User

class ProfileData(models.Model):
	user=models.OneToOneField(User)
	branch = models.CharField(max_length=200)
	enrollment = models.CharField(max_length=10)
	gender = models.CharField(max_length=6)
	dob = models.DateField()
	email=models.EmailField()
	contact=models.CharField(max_length=15)
	address=models.CharField(max_length=200)
	about=models.CharField(max_length=300)

