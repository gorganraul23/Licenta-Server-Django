from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Experiment
from .serializers import ExperimentDataSerializer
from api.models import Session


@api_view(['POST'])
def save_experiment_response(request):
    if request.method == 'POST':
        user_id = request.data['userId']
        session_id = request.data['sessionId']
        activity = request.data['activity']
        question_id = request.data['questionId']
        user_response = request.data['userResponse']

        print(user_id, session_id, activity, question_id, user_response)

        experiment_serializer = ExperimentDataSerializer(data=request.data)
        if experiment_serializer.is_valid():
            experiment_serializer.save()
            return Response(True, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def save_experiment_start_time(request):
    if request.method == 'POST':
        user = request.user
        session = Session.objects.filter(user=user, end_time__isnull=True).first()

        if session:
            experiment = Experiment.objects.filter(session=session, user=user)
            if experiment:
                experiment.delete()
            Experiment.objects.get_or_create(session=session, user=user)
            return Response(True, status=200)
        else:
            return Response(False, status=404)
