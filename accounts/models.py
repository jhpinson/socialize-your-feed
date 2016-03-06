# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from model_utils.models import TimeStampedModel

from django.db import models


class BaseSocialAccount(TimeStampedModel):
    user = models.ForeignKey('auth.User')
    name = models.CharField('Account name', max_length=128)
    real_type = models.ForeignKey(ContentType, editable=False, null=False, blank=True)

    def get_real_type(self):
        return ContentType.objects.get_for_model(self)

    def cast(self):

        # instance is already casted
        if self.get_real_type() == self.real_type:
            return self

        return self.real_type.get_object_for_this_type(pk=self.pk)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.real_type = self.get_real_type()

        super(BaseSocialAccount, self).save(*args, **kwargs)


class TwitterAccount(BaseSocialAccount):
    access_token_key = models.CharField(max_length=128)
    access_token_secret = models.CharField(max_length=128)
