from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from logapp.forms import UserForm
from django.contrib import messages
from django.contrib.auth.models import User
from logapp.forms import ProfileForm
# Create your views here.


def profile(request):
	if request.user.is_authenticated():
		request.session['username']=request.user.username
		return render(request,'logapp/profile.html',)
	else:
		request.session['state']="Please Log In below"
		username=''
		if(request.method=="POST"):
			username=request.POST.get('username')
			password=request.POST.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					request.session['state']="Login Successful"
					request.session['username']=username
					login(request, user)
					
					return render(request,'logapp/profile.html',{'username':username})
				else:
					request.session['state']="Your account is not active"
			else:
				messages.add_message(request,messages.ERROR,'Incorrect Login Credentials')
				#request.session['state']="Incorrect login credentials"
				return HttpResponseRedirect('../login/')
		
		
		return HttpResponseRedirect('../login/')
	
def complete(request):
	
