import re
from django.db.models.base import Model
from django.http import response
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .models import Challan
# Create your views here.


class ChallanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challan
        fields = ['challan_id', 'vehicle_number', 'vehicle_type', 'violation_type', 'challan_amount',
                  'challan_location', 'challan_status', 'challan_time']


class ChallanView(APIView):
    def get(self, request):
        challans_data = Challan.objects.all()
        get_serialized_chalans = ChallanSerializer(challans_data, many=True)
        return Response(get_serialized_chalans.data)

    def post(self, request):
        new_challan = ChallanSerializer(data=request.data)
        new_challan.is_valid(raise_exception=True)
        new_challan.save()
        return Response("Submited")


class ChallanViewDetail(APIView):
    def put(self, request, id):
        chalan_to_update = get_object_or_404(Challan, pk=id)
        get_updated_challan = ChallanSerializer(
            chalan_to_update, data=request.data)
        get_updated_challan.is_valid(raise_exception=True)
        get_updated_challan.save()
        return Response("Updated!")

    def delete(self, request, id):
        challan_to_delete = get_object_or_404(Challan, pk=id)
        challan_to_delete.delete()

    def get(self, request, id):
        get_specific_challan = get_object_or_404(Challan, pk=id)
        serialize_specific_challan = ChallanSerializer(get_specific_challan)
        return Response(serialize_specific_challan.data)
