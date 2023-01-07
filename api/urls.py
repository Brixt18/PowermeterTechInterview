# from rest_framework import routers

# from .viewsets import *

# router = routers.DefaultRouter()

# router.register("api/light-meter", LightMeterViewSet, "light-meter")
# router.register("api/measure", MeasureViewSet, "measure")

# urlpatterns = router.urls

from django.urls import path
from . import views

urlpatterns = [
    path('light-meter/', views.LightMeter.as_view(), ),
    path('light-meter/<id>/', views.LightMeter.as_view()),
    path('measure/', views.Measure.as_view()),
    path('measure/<id>/', views.Measure.as_view()),

    path('maximum-consumption/<id>/', views.maximum_consumption),
    path('manimum-consumption/<id>/', views.minimum_consumption),
    path('average-consumption/<id>/', views.average_consumption),
]