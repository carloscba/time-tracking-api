from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    client = models.ForeignKey('client.Client')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=16, null=True)
    url = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)