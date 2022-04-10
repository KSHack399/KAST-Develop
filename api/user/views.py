from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny

from user.models import User
from user.serializers import UserSerializer

class ListUser(APIView):

    permissions_classes = (AllowAny, )

    def get(self, request):
        user_list=User.objects.all().filter(status_delete=False)
        serializer = UserSerializer(user_list, many= True)
        return Response (serializer.data, status=status.HTTP_200_OK)

class RegisterUser(APIView):

    permissions_classes = (AllowAny, )

    def post(self, request ):
        serializer =UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data, status=status.HTTP_201_CREATED)