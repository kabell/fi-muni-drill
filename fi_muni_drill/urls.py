from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'fi_muni_drill.views.question'),
    
    url(r'^(\w+)/(\w+)/(\w+)$', 'fi_muni_drill.views.question'),
    url(r'^(\w+)/(\w+)/(\w+)/(\w+)/(\w+)$', 'fi_muni_drill.views.question'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
