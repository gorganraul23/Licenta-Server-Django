# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


@api_view(['POST'])
@csrf_exempt
def sensor_data(request):
    if request.method == 'POST':
        # Get the sensor data from the request body
        data = JSONParser().parse(request)
        print(data)

        # Return a JSON response indicating success
        return JsonResponse({'status': 'success'})
    else:
        # Return a JSON response indicating error
        return JsonResponse({'status': 'error'})
