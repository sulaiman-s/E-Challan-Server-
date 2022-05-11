from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .models import UserHistory,WardenHistory
# Create your views here.

class UserHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=UserHistory
        fields=['id','number','time','image','name']

class WardenHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model=WardenHistory
        fields=['id','number','type','time','name']

class UserHistoryView(APIView):
    def get(self,request):
        his=UserHistory.objects.all()
        s_his=UserHistorySerializer(his,many=True)
        return  Response(s_his.data)
    def post(self,request):
        s_his=UserHistorySerializer(data=request.data)
        s_his.is_valid(raise_exception=True)
        s_his.save()
        return  Response('history item saved')


class UserHistoryDelete(APIView):
    def delete(self,request,name):
        his_items=UserHistory.objects.filter(name__icontains=name)
        his_items.delete()
        return  Response('item deleted successfully')
    def get(self,request,name):
        his=UserHistory.objects.filter(name__icontains=name)
        s_his=UserHistorySerializer(his,many=True)
        return Response(s_his.data)


class WardenHistoryView(APIView):
    def get(self, request):
        his = WardenHistory.objects.all()
        s_his = WardenHistorySerializer(his, many=True)
        return Response(s_his.data)

    def post(self, request):
        s_his = WardenHistorySerializer(data=request.data)
        s_his.is_valid(raise_exception=True)
        s_his.save()
        return Response('history item saved')

class WardenHistoryDelete(APIView):
    def delete(self, request, name):
        his_items = WardenHistory.objects.filter(name__icontains=name)
        his_items.delete()
        return Response('item deleted successfully')

    def get(self,request,name):
        his=WardenHistory.objects.filter(name__contains=name)
        s_his=WardenHistorySerializer(his,many=True)
        return Response(s_his.data)
