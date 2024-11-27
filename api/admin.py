from django.contrib import admin

from .models import SensorData, Session

admin.site.register(SensorData)
admin.site.register(Session)
