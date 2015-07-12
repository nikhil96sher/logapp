from django.db import models
from django.contrib.auth.models import User

class ProfileData(models.Model):
	BRANCH_CHOICES=(('CSE','Computer Science and Engineering'),('ECE','ECE'),('CE','CE'),('ME','ME'))
	user=models.OneToOneField(User)
	branch = models.CharField(max_length=200,choices=BRANCH_CHOICES)
	enrollment = models.IntegerField()#min_value=1000000,max_value=99999999)
	gender = models.CharField(max_length=1,blank=False,choices=(('M','Male'),('F','Female')),default='M')
	dob = models.DateField()
	email=models.EmailField()
	contact=models.IntegerField(max_length=10)
	address=models.CharField(max_length=200)
	about=models.CharField(max_length=300)

