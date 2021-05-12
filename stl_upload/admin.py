# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Inputs, StlModels, UserProcess
# Register your models here.
admin.site.register(Inputs)
admin.site.register(StlModels)
admin.site.register(UserProcess)
