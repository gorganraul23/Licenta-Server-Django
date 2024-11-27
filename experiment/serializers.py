from rest_framework import serializers

from .models import ExperimentData


class ExperimentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentData
        fields = ('userId', 'sessionId', 'activity', 'questionId', 'userResponse')
