from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class LightMeterViewSet(ModelViewSet):
    queryset = LightMeter.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LightMeterSerializer


class MeasureViewSet(ModelViewSet):
    queryset = Measure.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MeasureSerializer
