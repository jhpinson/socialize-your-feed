# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from . import models


@admin.register(models.Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = 'url', 'last_fetch_date', 'created'


@admin.register(models.Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = 'feed', 'guid', 'title', 'publication_date', 'created'
