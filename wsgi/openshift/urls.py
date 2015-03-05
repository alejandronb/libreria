from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'openshift.views.home', name='home'),

    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^listado/$', 'openshift.libreria.views', name='listar_libros'),
    url(r'^listado/', 'openshift.libreria.views.listar_libros'),
    url(r'^registro/$', 'openshift.libreria.views.registro'),
    #url(r'^login/$', 'openshift.libreria.views.login2'),
    url(r'^$', 'openshift.libreria.views.login2'),

)
