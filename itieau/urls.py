from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'itieau_app.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='Login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}, name='Logout'),
    url(r'^admin/', include(admin.site.urls)),
)
