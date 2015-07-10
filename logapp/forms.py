from django.contrib.auth.models import User
from django.forms import ModelForm
from logapp.models import ProfileData
class UserForm(ModelForm):
	class Meta:
		model= User
		fields=('username','first_name','last_name','password','email')

class ProfileForm(ModelForm):
	class Meta:
		model=ProfileData
		fields=('branch','enrollment','gender','dob','email','contact','address','about')
	
