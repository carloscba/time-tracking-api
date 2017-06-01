from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Userbot(models.Model):
    name = models.CharField(max_length=255)
    platform_id = models.CharField(max_length=255)