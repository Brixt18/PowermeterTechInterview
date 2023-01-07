from django.utils import timezone
from django.db import models

STRING = models.CharField
DATETIME = models.DateTimeField
FLOAT = models.FloatField
FK = models.ForeignKey


class _Model(models.Model):
    created_at = DATETIME(auto_now_add=True)
    updated_at = DATETIME(default=timezone.now)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk is not None:
            self.updated_at = timezone.now()

        super().save(*args, **kwargs)

    def update(self, data: dict):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

        if hasattr(self, "updated_at"):
            self.updated_at = timezone.now()
        
        self.save()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)


class LightMeter(_Model):
    name = STRING(max_length=100)

    class Meta:
        db_table = "light_meter"


class Measure(_Model):
    light_meter_id = FK(LightMeter, on_delete=models.PROTECT, db_column="light_meter_id")
    kwh = FLOAT()

    class Meta:
        db_table = "measure"
