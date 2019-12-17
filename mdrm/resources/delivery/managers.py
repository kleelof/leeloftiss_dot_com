import datetime

from django.db import models
from mdrm.resources.delivery.models import *


class DeliveryWindowManager(models.Manager):
    def upcoming(self, start_date: datetime):
        return self.filter(open__gt=start_date)

    def get_window(self, window_id):
        windows = self.filter(id=window_id)
        return windows[0] if windows else None
