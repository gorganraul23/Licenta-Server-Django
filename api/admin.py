from django.contrib import admin

# Register your models here.
from api.models import SensorData, Session

admin.site.register(SensorData)
admin.site.register(Session)
