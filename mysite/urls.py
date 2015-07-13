from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
urlpatterns = patterns('',
    url(r'^logapp/',include('logapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
