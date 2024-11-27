from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ExperimentDataSerializer


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
