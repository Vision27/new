from rest_framework import serializers
from million.models import *
from django.contrib.auth.models import User


class Groups_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ('id', 'groups_style', 'groups_singers', 'groups_songs',)


class Concert_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = ('id', 'concert_date', 'concert_time', 'concert_place', 'group_concert',)


class Singer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ('id', 'singer_reputation', 'singer_age', 'singer_sex',)


class UserSerializer(serializers.ModelSerializer):
    singer_owner = serializers.PrimaryKeyRelatedField(many=True, queryset=Singer.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'singer_owner', 'password', 'email',)
