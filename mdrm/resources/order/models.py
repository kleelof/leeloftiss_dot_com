from django.db import models
from mdrm.mdrm import MDRMModel
from mdrm.resources.delivery.models import DeliveryWindow
from mdrm.resources.menu.models import Meal
from django.contrib.auth.models import User


class Order(MDRMModel):
    PENDING = 1
    CANCELED = 2
    COMPLETED = 3
    ASSEMBLING = 4

    STATUSES = (
        (PENDING, 'pending'),
        (CANCELED, 'canceled'),
        (COMPLETED, 'completed'),
        (ASSEMBLING, 'assembling')
    )

    status = models.SmallIntegerField(choices=STATUSES, default=ASSEMBLING)
    quantity = models.FloatField(default=0)

    meal = models.ForeignKey(Meal, related_name='order', on_delete=models.SET_NULL, null=True)
    delivery_window = models.ForeignKey(DeliveryWindow, related_name='order', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)