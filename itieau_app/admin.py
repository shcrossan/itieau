__author__ = 'shanecrossan'

#django
from django.contrib import admin

#local
from models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')
    search_fields = ('name', 'number',)


class UrlAdmin(admin.ModelAdmin):
    list_display = ('script',)
    filter_horizontal = ('contacts',)


admin.site.register(contact, ContactAdmin)
admin.site.register(Url, UrlAdmin)