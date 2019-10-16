from rest_framework import serializers
from million.models import *


class Groups_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ('groups_songs', 'groups_singers',)


class Concert_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = ('Concert_place', 'Concert_name', 'Concert_time', 'Concert_groups')


class Singer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ('singer_sex', 'singer_age', 'singer_style', 'singer_reputation', 'singer_price')
