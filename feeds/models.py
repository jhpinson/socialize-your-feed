# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models
from model_utils.models import TimeStampedModel


class Feed(TimeStampedModel):
    title = models.CharField('Feed title', max_length=256)
    url = models.URLField('feed URL')
    last_fetch_date = models.DateTimeField('Last fetched at', default=None, null=True, editable=None)

    def __str__(self):
        return self.title

class Entry(TimeStampedModel):

    class Meta:
        unique_together = ('feed', 'guid')

    feed = models.ForeignKey(Feed, verbose_name='Flux')
    guid = models.CharField('Glocal unique ID', max_length=256)
    title = models.CharField('Title', max_length=512)
    url = models.URLField('Entry URL')
    publication_date = models.DateTimeField('Publication date')
    raw = models.TextField('Raw feed entry', max_length=2048)