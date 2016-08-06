from django.contrib import admin
from . import models

class BotAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Bot,BotAdmin)

