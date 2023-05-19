from django.urls import re_path, path

from .consumers import SensorDataConsumer

websocket_urlpatterns = [
    re_path(r'ws/sensordata/$', SensorDataConsumer.as_asgi()),
]