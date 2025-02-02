from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import SensorData, Session


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ('id', 'session', 'hrv', 'hrvWithInvalid', 'hr', 'ibi', 'timestamp')


User = get_user_model()


class SessionSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Session
        fields = ('id', 'reference', 'start_time', 'end_time', 'user_email')
