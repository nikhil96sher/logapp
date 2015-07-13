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
		request.session['username']=request.user.username;
		return HttpResponseRedirect('../profile')
	elif request.method=="POST":
		signupform=UserForm(request.POST)
		if signupform.is_valid():
			new_user=User.objects.create_user(**signupform.cleaned_data)
			new_user.backend='django.contib.auth.backends.ModelBackend'
			messages.add_message(request,messages.SUCCESS,'Registration Successful !!')
			return HttpResponseRedirect('../welcome')
		else:
			return render(request,'logapp/welcome.html',{'form':signupform})	
 	else:
		signupform=UserForm()
		return render(request,'logapp/welcome.html',{'form':signupform})