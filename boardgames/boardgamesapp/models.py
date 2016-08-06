from __future__ import unicode_literals
from django.conf import settings
from django.db import models
import os

ROOT_BOT_PATH = "/home/boardgames/executables"
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class Bot(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL)
    bot_name = models.CharField(max_length=30)
    bot_folder = models.CharField(max_length=30)

    @property
    def path(self):
        return os.path.join(ROOT_BOT_PATH,self.bot_folder)

