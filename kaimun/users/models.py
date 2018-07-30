# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.encoding import python_2_unicode_compatible



@python_2_unicode_compatible
class User(AbstractUser):
    name = models.CharField(max_length=300, default=0)

    def __str__(self):
        return self.username











