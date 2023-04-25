from rest_framework import serializers

from api.models import SensorData, Session


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ('id', 'session', 'hrv', 'hr', 'ibi', 'timestamp')


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('id', 'start_time', 'end_time')
