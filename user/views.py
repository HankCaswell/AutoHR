from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST)
from django.contrib.auth.models import User
from unit.models import Unit 
from .serializers import UserRegistrationSerializer, UserProfileSerializer
from unit.serializers import UnitSerializer
# Create your views here.


class UserCreate(APIView): 

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data= request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user: 
                return Response({'User created': {user.username}}, HTTP_201_CREATED)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

class UnitCreate (APIView):
    def post(self, request, format='json'):
        serializer = UnitSerializer(data= request.data)
        if serializer.is_valid():
            unit = serializer.save()
            if unit: 
                return Response(serializer.data, HTTP_201_CREATED)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)