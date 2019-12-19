from django.db import models
from mdrm.mdrm import MDRMModel
from mdrm.resources.delivery.managers import DeliveryWindowManager
from django.template import defaultfilters


class DeliveryWindow(MDRMModel):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    date = models.DateField()
    open = models.TimeField()
    close = models.TimeField()

    objects = DeliveryWindowManager()

    def __str__(self):
        return f'{defaultfilters.date(self.date, "l M, j Y")}: {defaultfilters.date(self.open, "P")} - {defaultfilters.date(self.close, "P")}'