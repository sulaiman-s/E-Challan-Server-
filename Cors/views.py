from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from .models import ProfilePic
from django.shortcuts import render


def privacyPolicy(request):
    return  render(request,"privacyPolicy.html")





class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.username
        token['email'] = user.email
        token["is_admin"] = user.is_staff

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePic
        fields = ['id', 'name', 'profile_img']


class Profiles(APIView):
    def get(self, request):
        pf = ProfilePic.objects.all()
        pf_s = ProfileSerializer(pf, many=True)
        return Response(pf_s.data)

    def post(self, request):
        pf = ProfileSerializer(data=request.data)
        pf.is_valid(raise_exception=True)
        pf.save()
        return Response(pf.data)


class ProfilesSpec(APIView):
    def get(self, request, name):
        pf = ProfilePic.objects.filter(name__exact=name)
        pf_s = ProfileSerializer(pf, many=True)
        return Response(pf_s.data)

    def patch(self, request,id):
        pf_to_update = ProfilePic.objects.get(pk=id)
        pf_s = ProfileSerializer(pf_to_update, data=request.data,partial=True)
        pf_s.is_valid(raise_exception=True)
        pf_s.save()
        return Response(pf_s.data)

    def delete(self, request, id):
        pf_d = ProfilePic.objects.get(pk=id)
        pf_d.delete()
        return Response('deleted successfully')
