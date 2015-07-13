from django.conf.urls import patterns,url
from logapp import views

urlpatterns=patterns(
'',
url(r'^profile/edit/submit/$',views.profile_edit_submit,),
url(r'^profile/edit/$',views.profile_edit,name="edit_profile"),
url(r'^profile/edit/password/submit/$',views.password_change_submit),
url(r'^profile/edit/password/$',views.password_change,name="password_change"),
url(r'^profile/complete/submit/$',views.profile_complete,),
url(r'^profile/complete/$',views.profile_complete,name='profile_complete'),
url(r'^profile/$',views.profile,name='profile'),
url(r'^welcome/$',views.welcome,name='welcome'),
url(r'^logout/$',views.log_out,name='logout'),
)
