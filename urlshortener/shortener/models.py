from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import CharField

# Create your models here.


class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)
