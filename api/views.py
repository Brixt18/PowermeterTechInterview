from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from utils.formats import strip_dict_fields

from .models import LightMeter as LightMeterModel, Measure as MeasureModel
from .serializers import LightMeterSerializer, MeasureSerializer


class _Model(APIView):
    def _mapper(self, data: dict) -> dict:
        _data = {}

        for k, v in data.items():
            if k in self._fields:
               _data[k] = v

        return strip_dict_fields(_data)


class LightMeter(_Model):
    _fields = ('name',)

    def get(self, request, id=None):
        if id is None:
            data = LightMeterModel.objects.all()
            serializer = LightMeterSerializer(data, many=True)

        else:
            data = get_object_or_404(LightMeterModel, pk=id)
            serializer = LightMeterSerializer(data, many=False)

        return Response(serializer.data)

    def post(self, request):
        data = self._mapper(request.data)

        model: LightMeterModel = LightMeterModel(**data)
        model.save()

        return Response(status=201)

    def patch(self, request, id):
        obj: LightMeterModel = get_object_or_404(LightMeterModel, pk=id)

        data = self._mapper(request.data)

        obj.update(data)

        return Response(status=204)

    def delete(self, request, id):
        obj: LightMeterModel = get_object_or_404(LightMeterModel, pk=id)

        obj.delete()

        return Response(status=204)


class Measure(_Model):
    _fields = ('light_meter_id', 'kwh')

    def get(self, request, id=None):
        if id is None:
            data = MeasureModel.objects.filter(kwh__gte=0).all()
            serializer = MeasureSerializer(data, many=True)

            # for measure in serializer.data:
            #     print(measure.kwh)

        else:
            data = get_object_or_404(MeasureModel, pk=id)
            serializer = MeasureSerializer(data, many=False)

        return Response(serializer.data)

    def post(self, request):
        data = self._mapper(request.data)
        data["light_meter_id"] = get_object_or_404(
            LightMeterModel, pk=data["light_meter_id"])

        model: MeasureModel = MeasureModel(**data)
        model.save()

        return Response(status=201)

    def patch(self, request, id):
        obj: MeasureModel = get_object_or_404(MeasureModel, pk=id)

        data = self._mapper(request.data)
        if data.get("light_meter_id"):
            data["light_meter_id"] = get_object_or_404(
                LightMeterModel, pk=data["light_meter_id"])

        obj.update(data)

        return Response(status=204)

    def delete(self, request, id):
        obj: MeasureModel = get_object_or_404(MeasureModel, pk=id)

        obj.delete()

        return Response(status=204)


@api_view(["GET"])
def maximum_consumption(request, id):
    light_meter: LightMeterModel = get_object_or_404(LightMeterModel, pk=id)

    query: MeasureModel = MeasureModel.objects.filter(
        light_meter_id=light_meter.id).order_by("-kwh").first()

    return Response({
        "maximum_consumption": f"{query.kwh}kWh",
    })


@api_view(["GET"])
def minimum_consumption(request, id):
    light_meter: LightMeterModel = get_object_or_404(LightMeterModel, pk=id)

    query: MeasureModel = MeasureModel.objects.filter(
        light_meter_id=light_meter.id).order_by("kwh").first()

    return Response({
        "minimum_consumption": f"{query.kwh}kWh",
    })


@api_view(["GET"])
def total_consumption(request, id):
    light_meter: LightMeterModel = get_object_or_404(LightMeterModel, pk=id)

    query: MeasureModel = MeasureModel.objects.filter(
        light_meter_id=light_meter.id).all()

    total = sum([x.kwh for x in query])

    return Response({
        "total_consumption": f"{total}kWh",
    })


@api_view(["GET"])
def average_consumption(request, id):
    light_meter: LightMeterModel = get_object_or_404(LightMeterModel, pk=id)

    query: MeasureModel = MeasureModel.objects.filter(light_meter_id=light_meter.id).all()

    average = round(sum([x.kwh for x in query])/len(query), 2)

    return Response({
        "total_consumption": f"{average}kWh",
    })
