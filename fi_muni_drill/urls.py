from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'fi_muni_drill.views.index'),
    url(r'^question$', 'fi_muni_drill.views.question'),

    # Examples:
    # url(r'^$', 'fi_muni_drill.views.home', name='home'),
    # url(r'^fi_muni_drill/', include('fi_muni_drill.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
