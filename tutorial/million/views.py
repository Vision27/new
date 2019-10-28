from million.models import *
from million.serializers import *
from rest_framework import generics
from rest_framework.response import *
from django.http import Http404
from rest_framework.views import APIView
import re
from django.contrib.auth.models import User
from million.serializers import UserSerializer
from rest_framework import permissions

permission_classes = [permissions.IsAuthenticatedOrReadOnly]
phone_validatior = input()


def abc(phone_validator):
    if len(phone_validatior):
        return False
    result = re.findall(r'\+996\d{9}', phone_validatior)
    return len(result) > 0


class GroupsView(generics.ListCreateAPIView):
    queryset = Groups.objects.all()
    serializer_class = Groups_Serializer


class ConcertView(generics.ListCreateAPIView):
    queryset = Concert.objects.all()
    serializer_class = Concert_Serializer


class SingerView(generics.ListCreateAPIView):
    queryset = Singer.objects.all()
    serializer_class = Singer_Serializer

    def perform_create(self, serializer):

        serializer.save(owner=self.request.user)
    # def get(self, request):
    #     return Response("Daa")
    #
    # def post(self, request):
    #     num = (request.data['number'])
    #     answer = abc(num)
    #     if answer == True:
    #         serializers = Singer_Serializer(data = request.data)
    #         if serializers.is_valid():
    #             serializers.save()
    #
    #             return Response('yuhu')
    #         else:
    #             return Response('no yuhu')


class ConcertView(generics.ListCreateAPIView):
    queryset = Concert.objects.all()
    serializer_class = Concert_Serializer


class Singerdetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Singer.objects.all()
    serializer_class = Singer_Serializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
