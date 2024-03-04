
from rest_framework import serializers
from .models import *



class CampStationsStatusSerializers(serializers.Serializer):
    HCID = serializers.IntegerField()
    TeamId = serializers.IntegerField()
    Date = serializers.IntegerField()
