from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,Http404
from logapp.forms import UserForm
from django.contrib import messages
from django.contrib.auth.models import User
from logapp.forms import ProfileForm
from logapp.models import ProfileData
# Create your views here.


def profile(request):
	if request.user.is_authenticated():
		request.session['username']=request.user.username
		try:
			profiledata=get_object_or_404(ProfileData,user=request.user)
		except(Http404):
			return HttpResponseRedirect('./complete')
		return render(request,'logapp/profile.html',{'profile':profiledata})
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
					try:
						profiledata=get_object_or_404(ProfileData,user=request.user)
					except(Http404):
						return HttpResponseRedirect('./complete')
									
					return render(request,'logapp/profile.html',{'profile':profiledata})
				else:
					request.session['state']="Your account is not active"
			else:
				messages.add_message(request,messages.ERROR,'Incorrect Login Credentials')
				#request.session['state']="Incorrect login credentials"
				return HttpResponseRedirect('../login/')
		
		
		return HttpResponseRedirect('../login/')


def complete(request):
	try:
		profiledata=get_object_or_404(ProfileData,user=request.user)
		return HttpResponseRedirect('../welcome')
	except(Http404):
		form=ProfileForm()
		return render(request,'logapp/complete.html',{'form':form})


def submit_profile(request):
	form=ProfileForm(request.POST)
	if form.is_valid():
		new_profile=ProfileData.objects.create(user=request.user,branch=request.POST['branch'],enrollment=request.POST['enrollment'],gender=request.POST['gender'],dob=request.POST['dob'],email=request.POST['email'],contact=request.POST['contact'],address=request.POST['address'],about=request.POST['about'])
		return HttpResponseRedirect('../../../welcome')	
	else:
		return HttpResponseRedirect('../../complete')

def password_change(request):
	return render(request,'logapp/password.html',)

def profile_edit(request):
	profiledata=get_object_or_404(ProfileData,user=request.user)
	form=ProfileForm()
	return render(request,'logapp/profile_edit.html',{'profile':profiledata,'form':form})

def profile_edit_submit(request):
	try:
		profiledata=get_object_or_404(ProfileData,user=request.user)
		if request.POST['branch']=="":
			return HttpResponseRedirect("../../")
		else:
			profiledata.branch=request.POST['branch']
			profiledata.save()
			return HttpResponseRedirect("../../")
	except(Http404):
		return HttpResponseRedirect("../../../login")

def password_change_submit(request):
	if(request.method=="POST"):
		
		try:
			if(request.POST['newpassword']!=request.POST['newpassword2']):
				messages.add_message(request,messages.ERROR,'Password and Confirm Password Don\'t Match ')
				return HttpResponseRedirect("../")
			user=authenticate(username=request.user.username,password=request.POST['oldpassword'])
			if user is not None:
				#if hash(request.POST['oldpassword'])==request.user.password:
				#request.user.password=hash(request.POST['newpassword'])
				user.set_password(request.POST['newpassword'])
				user.save()
				login(request,user)
				#request.user.save()
				return HttpResponseRedirect("../../../")
			else:
				messages.add_message(request,messages.ERROR,'Incorrect Password')
				return HttpResponseRedirect("../")
		except(Http404):
			return HttpResponseRedirect("../../../../login")

	else:
		return HttpResponseRedirect("../../../../profile")
