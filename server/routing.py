from django.urls import re_path

from manage import myWSInstance, myAngularWSInstance

websocket_urlpatterns = [
    re_path(r'ws/sensordata/$', myWSInstance),
    re_path(r'ws/realtime/$', myAngularWSInstance)
]
