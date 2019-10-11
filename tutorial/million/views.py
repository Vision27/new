
from million.models import *
from million.serializers import *
from rest_framework import generics
from rest_framework.response import *

from django.http import Http404
from rest_framework.views import APIView

class SexView(generics.ListAPIView):
    queryset =Sex.objects.all()
    serializer_class = Sex_Serializer
    