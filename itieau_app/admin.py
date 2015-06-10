__author__ = 'shanecrossan'

#django
from django.contrib import admin

#local
from models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')
    search_fields = ('name', 'number',)

admin.site.register(contact, ContactAdmin)