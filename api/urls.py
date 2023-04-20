from django.urls import path

from api.views import sensor_data

urlpatterns = [
    path('sensor-data', sensor_data),
]
