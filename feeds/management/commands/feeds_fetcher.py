# encoding: utf-8
from __future__ import unicode_literals, absolute_import

import datetime
import feedparser

from dateutil import parser

from django.core.management.base import BaseCommand
from django.db import transaction
from django.db.utils import IntegrityError
from django.utils import timezone

from feeds.models import Feed, Entry


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for feed in Feed.objects.all():
            self._fetch_feed(feed)

    @transaction.atomic
    def _fetch_feed(self, feed):

        feed.last_fetch_date = timezone.now()

        for entry in feedparser.parse(feed.url)['entries']:
            title = entry['title']
            guid = entry['guid']
            publication_date = parser.parse(entry['published'])
            url = entry['link']

            try:
                Entry.objects.create(feed=feed, guid=guid, title=title, publication_date=publication_date, url=url)
            except IntegrityError:
                pass

        feed.save()
