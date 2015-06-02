from django.db import models
from django.contrib.auth.models import User

class domain(models.Model):
    domain = models.CharField(max_length=120, null=False, blank=False)
    user = models.ManyToManyField(User)

    def __unicode__(self):
        return self.domain