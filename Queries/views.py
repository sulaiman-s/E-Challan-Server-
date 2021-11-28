from django.db.models import fields
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .models import MLImages, Queries, Uploads
# Create your views here.


class QueriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queries
        fields = ['name', 'email', 'mesage']


class UploadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uploads
        fields = ['vehicle_number', 'challan_image']


class MLImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MLImages
        fields = ['ml_image']


class QueriesView(APIView):
    def get(self, request):
        Queries_data = Queries.objects.all()
        get_serialized_Query = QueriesSerializer(Queries_data, many=True)
        return Response(get_serialized_Query.data)

    def post(self, request):
        new_Query = QueriesSerializer(data=request.data)
        new_Query.is_valid(raise_exception=True)
        new_Query.save()
        return Response("Submited")


class UploadsView(APIView):
    def get(self, request):
        uploads_data = Uploads.objects.all()
        get_serialized_uploads = UploadsSerializer(uploads_data, many=True)
        return Response(get_serialized_uploads.data)

    def post(self, request):
        new_upload = UploadsSerializer(data=request.data)
        new_upload.is_valid(raise_exception=True)
        new_upload.save()
        return Response("Submited")


class MLImageView(APIView):
    def get(self, request):
        images_data = MLImages.objects.all()
        get_serialized_images = MLImagesSerializer(images_data, many=True)
        return Response(get_serialized_images.data)

    def post(self, request):
        new_image = MLImagesSerializer(data=request.data)
        new_image.is_valid(raise_exception=True)
        new_image.save()
        return Response("will create a model to return vehicle number")
