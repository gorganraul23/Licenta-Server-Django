from django.http import JsonResponse
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from .serializers import UserSerializer, UserRegisterSerializer


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email, password=password)
            refresh = RefreshToken.for_user(user)
            return JsonResponse({'access_token': str(refresh.access_token), 'user_id': user.id},
                                status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LoginViewWeb(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email, password=password)
            refresh = RefreshToken.for_user(user)
            return JsonResponse({'access_token': str(refresh.access_token),
                                 'user_id': user.id,
                                 'is_superuser': user.is_superuser})
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'})


class RegisterView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        users_serializer = UserRegisterSerializer(data=data)
        user_dto_serializer = UserSerializer(data=data)
        if users_serializer.is_valid() and user_dto_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(user_dto_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse({'error': 'Already this email'})


@api_view(['GET', 'DELETE'])
def users_all(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def users_by_id(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
