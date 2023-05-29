from django.urls import re_path

from manage import myWSInstance

websocket_urlpatterns = [
    # path("ws/<str:channel_name>/", AngularConsumer.as_asgi()),
    re_path(r'ws/sensordata/$', myWSInstance),
]
