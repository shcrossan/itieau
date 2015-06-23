from django.db import models
from django.contrib.auth.models import User

class contact(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField("Nom", max_length=30)
    position = models.CharField("Role",max_length=30, null=True, blank=True)
    number = models.CharField("Numero", max_length=8, null=False, blank=False)

    def __unicode__(self):
        return self.name



class Url(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=32, null=True, blank=False)
    script = models.CharField(max_length=30, null=False, blank=False, help_text="Name of php script on other server with .php extension")
    position = models.IntegerField(max_length=2, null=True, blank=True)
    bornierSpilt = models.IntegerField(max_length=2, null=True, blank=False)
    contacts = models.ManyToManyField(contact)

    def __unicode__(self):
        return self.script