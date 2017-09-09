# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class product(models.Model):
    pid=models.IntegerField (primary_key=True)
    pname=models.CharField(max_length=20)
    pcost=models.DecimalField(max_digits=10, decimal_places=4)
    pfmd=models.DateField()
    pexpdt=models.DateField()