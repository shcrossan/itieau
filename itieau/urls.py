from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'itieau_app.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='Login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}, name='Logout'),
    url(r'^contact/$', 'itieau_app.views.addContact', name='contact'),
    url(r'^contact/delete/(?P<id>[0-9]+)$', 'itieau_app.views.deleteContact', name='DeleteContact'),
    url(r'^contact/edit/(?P<id>[0-9]+)$', 'itieau_app.views.editContact', name='EditContact'),
    url(r'^admin/', include(admin.site.urls)),

    #URL's for each Maire
    url(r'^faaa/$', 'itieau_app.views.faaa', name='faaa'),
    url(r'^demo/$', 'itieau_app.views.demo', name='demo'),
)
