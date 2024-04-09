from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST)
from django.contrib.auth.models import User
from .models import Unit 
from .serializers import UserRegistrationSerializer, UserProfileSerializer, FileUploadSerializer
from .serializers import UnitSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from autoHR.utils.pdf_parser import extract_text_from_pdf
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
    


class CreateUnitView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = UnitSerializer(data= request.data)
        if serializer.is_valid():
            unit = serializer.save()
            return Response({'unit_id': unit.id}, status =HTTP_201_CREATED)
        return Response(serializer.errors, status = HTTP_400_BAD_REQUEST)

class UnitListView(ListAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class PDFTextView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            extracted_text = extract_text_from_pdf(file)
            return Response({"extracted text": extracted_text}, status=HTTP_200_OK)
        else: 
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        

        