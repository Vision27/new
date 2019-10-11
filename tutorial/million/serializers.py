from rest_framework import  serializers
from million.models import *


class Sex_Serializer(serializers.ModeSerializer):
    class Meta:
        model=Sex
        fields=('sex_name',)