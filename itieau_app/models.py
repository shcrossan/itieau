from django.db import models
from django.contrib.auth.models import User

class contact(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField("Nom", max_length=30)
    position = models.CharField("Role",max_length=30, null=True, blank=True)
    number = models.CharField("Numero", max_length=8, null=False, blank=False)