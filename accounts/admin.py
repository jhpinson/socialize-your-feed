# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from . import models

@admin.register(models.TwitterAccount)
class TwitterAccountAdmin(admin.ModelAdmin):

    list_display = 'user', 'name', 'created'