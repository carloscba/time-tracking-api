from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
