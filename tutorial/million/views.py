from million.models import *
from million.serializers import *
from rest_framework import generics
from rest_framework.response import *

from django.http import Http404
from rest_framework.views import APIView


class GroupsView(generics.ListCreateAPIView):
    queryset = Groups.objects.all()
    serializer_class = Groups_Serializer


class ConcertView(generics.ListCreateAPIView):
    queryset = Concert.objects.all()
    serializer_class = Concert_Serializer


class SingerView(generics.ListCreateAPIView):
    queryset = Singer.objects.all()
    serializer_class = Singer_Serializer


