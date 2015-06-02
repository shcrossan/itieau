__author__ = 'shanecrossan'

#django
from django.contrib import admin

#local
from models import *

class DomainAdmin(admin.ModelAdmin):
    search_fields = ('domain',)
    filter_horizontal = ('user',)
    list_display = ('domain',)

admin.site.register(domain, DomainAdmin)