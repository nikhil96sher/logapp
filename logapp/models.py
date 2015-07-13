from django.db import models
from django.contrib.auth.models import User

class ProfileData(models.Model):
	BRANCH_CHOICES=(('CSE','Computer Science and Engineering'),('ECE','ECE'),('CE','CE'),('ME','ME'))
	user=models.OneToOneField(User)
	branch = models.CharField(max_length=200,choices=BRANCH_CHOICES)
	enrollment = models.IntegerField()#min_value=1000000,max_value=99999999)
	gender = models.CharField(max_length=6,blank=False,choices=(('Male','Male'),('Female','Female')),default='Male')
	dob = models.DateField()
	contact=models.CharField(max_length=15)
	address=models.CharField(max_length=200)
	about=models.CharField(max_length=300)

class Uploads(models.Model):
	user=models.OneToOneField(User)
	cover=models.ImageField(upload_to='./cover/',default='/media/cover/default_cover.jpg')
	profile=models.ImageField(upload_to='./profile/',default='/media/profile/default_profile.jpg')
