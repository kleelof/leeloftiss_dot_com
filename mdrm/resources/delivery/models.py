from django.db import models
from mdrm.mdrm import MDRMModel


class DeliveryWindow(MDRMModel):
    active = models.BooleanField(default=True)
    open = models.DateTimeField()
    close = models.DateTimeField()