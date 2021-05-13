# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Inputs(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    input1 = models.CharField(max_length=100)
    input2 = models.CharField(max_length=100)
    input3 = models.CharField(max_length=100)


class StlModels(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    filename = models.CharField(max_length=30)


class UserProcess(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    center_x = models.IntegerField()
    center_y = models.IntegerField()
    center_z = models.IntegerField()
    orientation_x = models.FloatField()
    orientation_y = models.FloatField()
    orientation_z = models.FloatField()
    opacity = models.FloatField()
    filename = models.CharField(max_length=100)


class UserStl(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stl_file = models.CharField(max_length=100)
