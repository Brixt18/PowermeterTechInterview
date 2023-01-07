from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import *


class LightMeterSerializer(ModelSerializer):
    class Meta:
        model = LightMeter
        fields = ('id', 'name')


class MeasureSerializer(ModelSerializer):
    class Meta:
        model = Measure
        fields = ('id', 'kwh', 'light_meter_id', 'created_at')
