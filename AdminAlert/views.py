from dataclasses import field
from django.shortcuts import render
from AdminAlert.models import AdminAlerts
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
# Create your views here.

class AlertsSerializers(serializers.ModelSerializer):
    class Meta:
        model=AdminAlerts
        fields=['Alert_Message','Alert_Image']

class AlertsView(APIView):
    def get(self,request):
        allAlerts=AdminAlerts.objects.last()
        alertserial=AlertsSerializers(allAlerts)
        return Response(alertserial.data)
