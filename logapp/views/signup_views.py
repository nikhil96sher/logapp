from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from logapp.forms import UserForm
from django.contrib import messages
from django.contrib.auth.models import User
from logapp.forms import ProfileForm
# Create your views here.

def signup(request):
	if request.user.is_authenticated():
		request.session['username']=request.user.username
		return HttpResponseRedirect('../profile')
	#request.session['signupstate']="Please fill the details"
	form=UserForm()
	return render(request,'logapp/signup.html',{'form':form})

def register(request):
	if(request.method=="POST"):
		form=UserForm(request.POST)
		if form.is_valid():
			new_user=User.objects.create_user(**form.cleaned_data)
			new_user.backend='django.contib.auth.backends.ModelBackend'
			#authenticate(username=new_user.username,password=new_user.password)
			#login(request,new_user)
			request.session['signupstate']="Successfully Registered !!"
			#request.session['username']=new_user.username
			messages.add_message(request,messages.SUCCESS,'Registration Successful !!')
			return HttpResponseRedirect('../login')
		else:
			request.session['signupstate']="Some Error Occured"
			return HttpResponseRedirect('../signup')	
	else:
		form=UserForm()
		return HttpResponseRedirect('../signup')
