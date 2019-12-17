from django.db import models
from mdrm.mdrm import MDRMModel
from mdrm.resources.menu.models import Meal
from mdrm.resources.delivery.managers import DeliveryWindowManager
from django.template import defaultfilters


class DeliveryWindow(MDRMModel):
    name = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    open = models.DateTimeField()
    close = models.DateTimeField()

    meals = models.ManyToManyField(Meal, related_name='delivery_windows')
    object = DeliveryWindowManager()

    def __str__(self):
        return f'{defaultfilters.date(self.open, "l M, j Y")}: {defaultfilters.date(self.open, "P")} - {defaultfilters.date(self.close, "P")}'