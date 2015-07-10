from django.conf.urls import patterns,url
from logapp import views

urlpatterns=patterns('',url(r'^register',views.register,name='register'),url(r'^signup/$',views.signup,name='signup'),url(r'^login/$',views.log_in,name='login'),url(r'^profile/$',views.profile,name='profile'),url(r'^welcome/$',views.welcome,name='welcome'),url(r'^logout/$',views.log_out,name='logout'),)
