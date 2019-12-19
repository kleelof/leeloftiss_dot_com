import datetime
from django.db import models
from mdrm.resources.menu.models import Meal


class DeliveryWindowManager(models.Manager):

    """
        [
            {
                window: {window},
                associated_meals: [
                    {meal}, {meal}
                ]
            }
        ]
    """
    def upcoming(self, start_date: datetime, end_date: datetime = None):
        if not end_date:
            windows = self.filter(date__gte=start_date)
        else:
            windows = self.filter(date__gte=start_date, date__lte=end_date)
        if not windows:
            return None
        for window in windows:
            yield {
                'window': window,
                'associated_meals': list(Meal.objects.filter(serve_start__lte=window.date, serve_end__gte=window.date))
            }


    def get_window(self, window_id):
        windows = self.filter(id=window_id)
        return windows[0] if windows else None
