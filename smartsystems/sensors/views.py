

from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import SensorData
from .serializers import SensorDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response




class SensorDataViewSet(APIView):
    
    def get(self, request):
        sensor_data = SensorData.objects.order_by('-created_at')[:20]  # Get the latest 10 sensor data entries
        serializer = SensorDataSerializer(sensor_data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    
