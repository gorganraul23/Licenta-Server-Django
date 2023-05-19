# Create your views here.
import asyncio
import json


from asgiref.sync import async_to_sync
import websocket
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from api.models import Session, SensorData
from api.serializers import SensorDataSerializer, SessionSerializer
from server.consumers import SensorDataConsumer


##############################################################

@api_view(['POST'])
def send_sensor_data(request):

    # sensor_data_consumer = SensorDataConsumer()
    # async_to_sync(sensor_data_consumer.send_message('message'))
    message = "Hello from Django to Unity!"
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("unity", {"type": "unity.message", "message": message})

    # asyncio.run(sensor_data_consumer.send('hello'))

    return Response({'success': True})


#######################################################################


@api_view(['POST'])
def start_session(request):
    session = Session()
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
    session_id = request.data['sessionId']
    hrv = request.data['hrv']
    hr = request.data['hr']
    ibi = request.data['ibi']

    session = Session.objects.get(id=session_id)
    sensor_data = SensorData(session=session, hrv=hrv, hr=hr, ibi=ibi)
    sensor_data.save()

    sensor_data_consumer = SensorDataConsumer()
    async_to_sync(sensor_data_consumer.send_data({'message': 'Hello, world!'}))

    return Response({'success': True})


@api_view(['GET', 'POST', 'DELETE'])
def sensor_data_list(request):
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
def sensor_data_object(request, id):
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


@api_view(['GET'])
def sensor_data_by_session(request, session):
    data = SensorData.objects.filter(session=session)

    if request.method == 'GET':
        sensor_data_serializer = SensorDataSerializer(data, many=True)
        return Response(sensor_data_serializer.data)

    if request.method == 'DELETE':
        data.delete()
        return Response({'message': 'Records were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def session_list(request):
    if request.method == 'GET':
        data = Session.objects.all().order_by('start_time')
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
