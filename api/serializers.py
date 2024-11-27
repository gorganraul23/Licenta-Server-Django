from rest_framework import serializers

from .models import SensorData, Session


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ('id', 'session', 'hrv', 'hr', 'ibi', 'timestamp')


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('id', 'reference', 'start_time', 'end_time')
