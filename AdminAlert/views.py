from dataclasses import field
from django.shortcuts import render
from AdminAlert.models import AlertImage, AlertMessage
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
# Create your views here.


class AlertsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = AlertImage
        fields = ['Alert_Image']


class AlertsMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = AlertMessage
        fields = ['id', 'Alert_Message']


class AlertsImageView(APIView):
    def get(self, request):
        allAlerts = AlertImage.objects.last()
        alertserial = AlertsImageSerializers(allAlerts)
        return Response(alertserial.data)


class AlertsMessageView(APIView):
    def get(self, request):
        allAlerts = AlertMessage.objects.all()
        alertserial = AlertsMessageSerializers(allAlerts, many=True)
        return Response(alertserial.data)
