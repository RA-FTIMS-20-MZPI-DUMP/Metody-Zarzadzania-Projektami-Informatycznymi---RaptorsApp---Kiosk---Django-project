from django.contrib import admin
from .models import KioskModel, KioskUser

admin.site.register(KioskModel)
admin.site.register(KioskUser)

