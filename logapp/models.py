from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
def contact_range(value):
	if value<10000000000 or value>9999999999:
		raise ValidationError("Enter a valid Contact Number")

def enroll_range(value):
	if value<10000000 or value>99999999:
		raise ValidationError("Enter a valid Enrollment Number")

class ProfileData(models.Model):	
	BRANCH_CHOICES=(('CSE','CSE'),('ECE','ECE'),('CE','CE'),('ME','ME'))
	user=models.OneToOneField(User)
	branch = models.CharField(max_length=200,choices=BRANCH_CHOICES)
	enrollment = models.IntegerField()#validators=[enroll_range])#min_value=10000000,max_value=99999999)
	gender = models.CharField(max_length=6,blank=False,choices=(('Male','Male'),('Female','Female')),default='Male')
	dob = models.DateField()
	contact=models.BigIntegerField()#validators=[contact_range])#min_value=1000000000,max_value=9999999999)
	address=models.CharField(max_length=200)
	about=models.CharField(max_length=300)

class Uploads(models.Model):
	user=models.OneToOneField(User)
	cover=models.ImageField(upload_to='./cover/',default='/cover/default_cover.jpg')
	profile=models.ImageField(upload_to='./profile/',default='/profile/default_profile.jpg')
