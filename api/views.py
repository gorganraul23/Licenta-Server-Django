# Create your views here.
import asyncio

from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Session, SensorData, PpgGreenData
from .serializers import SensorDataSerializer, SessionSerializer
from manage import myWSInstance, myAngularWSInstance
from users.models import User
from experiment.models import Experiment

number_of_lower = 0


@api_view(['POST'])
def start_session(request, id):
    session = Session.objects.create()
    user = User.objects.get(pk=id)
    session.user = user
    session.save()

    return Response({'session_id': session.id})


@api_view(['PUT'])
def set_ref_hrv_for_session(request):
    session_id = request.data["sessionId"]
    reference = request.data["hrv"]

    session = Session.objects.get(id=session_id)
    session.reference = reference
    session.save()

    return Response({'session_id': session.id})


@api_view(['PUT'])
def end_session(request, id):
    try:
        session = Session.objects.get(pk=id)
    except Session.DoesNotExist:
        return Response({'message': 'The session does not exist'}, status=status.HTTP_404_NOT_FOUND)

    session.end_time = timezone.now()
    session.save()

    return Response({'session_id': session.id})


@api_view(['POST'])
def save_sensor_data(request):
    global number_of_lower

    session_id = request.data['sessionId']
    hrv = request.data['hrv']
    hr = request.data['hr']
    ibi = request.data['ibi']
    ibi_status = request.data['ibiStatus']
    message = 'OK'
    print(ibi_status)

    session = Session.objects.get(id=session_id)
    sensor_data = SensorData(session=session, hrv=hrv, hr=hr, ibi=ibi, ibiStatus=ibi_status)
    # if session.reference != 0:
    sensor_data.save()

    if session.reference - hrv >= 20.0:
        number_of_lower += 1
    else:
        number_of_lower = 0

    if number_of_lower == 5:
        message = 'Decrease'
        number_of_lower = 0
    else:
        message = 'OK'

    if myWSInstance.connected:
        asyncio.run(myWSInstance.send_message(hr, hrv, message))
    if myAngularWSInstance.connected:
        asyncio.run(myAngularWSInstance.send_data(hr, hrv))

    return Response({'success': True})


@api_view(['POST'])
def save_ppg_green_data(request):
    session_id = request.data['sessionId']
    ppg_values = request.data['ppgValues']

    try:
        session = Session.objects.get(id=session_id)
    except Session.DoesNotExist:
        return Response({'error': 'Session not found'}, status=400)

    print(f"Received {len(ppg_values)} PPG values")
    for value in ppg_values:
        PpgGreenData.objects.create(session=session, ppg_value=value)

    return Response({'success': True})


@api_view(['GET', 'POST', 'DELETE'])
def sensor_data_all(request):
    if request.method == 'GET':
        data = SensorData.objects.all()
        sensor_data_serializer = SensorDataSerializer(data, many=True)
        return Response(sensor_data_serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        sensor_data_serializer = SensorDataSerializer(data=data)
        if sensor_data_serializer.is_valid():
            sensor_data_serializer.save()
            return Response(sensor_data_serializer.data, status=status.HTTP_201_CREATED)
        return Response(sensor_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = SensorData.objects.all().delete()
        return Response({'message': '{} Records were deleted successfully!'.format(count[0])},
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def sensor_data_by_id(request, id):
    try:
        sensor_data = SensorData.objects.get(pk=id)
    except SensorData.DoesNotExist:
        return Response({'message': 'The record does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        sensor_data_serializer = SensorDataSerializer(sensor_data)
        return Response(sensor_data_serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        sensor_data_serializer = SensorDataSerializer(sensor_data, data=data)
        if sensor_data_serializer.is_valid():
            sensor_data_serializer.save()
            return Response(sensor_data_serializer.data)
        return Response(sensor_data_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        sensor_data.delete()
        return Response({'message': 'Record was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def sensor_data_by_session(request, id):
    try:
        session = Session.objects.get(pk=id)
    except Session.DoesNotExist:
        return Response({'message': 'The session does not exist'}, status=status.HTTP_404_NOT_FOUND)
    data = SensorData.objects.filter(session=session)
    data = data.order_by('timestamp')

    if request.method == 'GET':
        sensor_data_serializer = SensorDataSerializer(data, many=True)
        return Response(sensor_data_serializer.data)

    if request.method == 'DELETE':
        data.delete()
        return Response({'message': 'Records were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def session_all(request):
    if request.method == 'GET':
        user = request.user
        if user.is_superuser:
            data = Session.objects.all().order_by('-start_time')
        else:
            data = Session.objects.filter(user=user).order_by('-start_time')

        session_serializer = SessionSerializer(data, many=True)
        return Response(session_serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        session_serializer = SessionSerializer(data=data)
        if session_serializer.is_valid():
            session_serializer.save()
            return Response(session_serializer.data, status=status.HTTP_201_CREATED)
        return Response(session_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = SensorData.objects.all().delete()
        return Response({'message': '{} Records were deleted successfully!'.format(count[0])},
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
def session_by_id(request, id):
    try:
        session = Session.objects.get(pk=id)
    except Session.DoesNotExist:
        return Response({'message': 'The session does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        session_serializer = SessionSerializer(session)
        return Response(session_serializer.data)

    if request.method == 'DELETE':
        session.delete()
        return Response({'message': 'Record was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def session_running(request):
    if request.method == 'GET':
        user = request.user
        session = Session.objects.filter(user=user, end_time__isnull=True).first()

        if session:
            session_serializer = SessionSerializer(session)
            experiment = Experiment.objects.filter(session=session, user=user)
            if experiment:
                experiment.delete()
            Experiment.objects.get_or_create(session=session, user=user)
            return Response(session_serializer.data)
        else:
            return Response({'error': 'No active session found.'}, status=404)
