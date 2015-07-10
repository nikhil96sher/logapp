from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from logapp.forms import UserForm
from django.contrib import messages
from django.contrib.auth.models import User
from logapp.forms import ProfileForm
# Create your views here.

def welcome(request):
	if request.user.is_authenticated():
		request.session['username']=request.user.username
		return HttpResponseRedirect('../profile/')
	return render(request,'logapp/welcome.html',)

def log_in(request):
	if request.user.is_authenticated():
		request.session['username']=request.user.username
		return HttpResponseRedirect('../profile/')
		#return render(request,'logapp/profile.html',)
	else:
		messages.add_message(request,messages.SUCCESS,'Please Log In Below')
		#request.session['state']="Please Log In Below"
		return render(request,'logapp/login.html',)

def log_out(request):
	logout(request)
	return HttpResponseRedirect('../welcome/')
