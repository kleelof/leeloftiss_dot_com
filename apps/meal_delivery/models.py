from django.db import models
from mdrm.models import Meal


class MealInfo(models.Model):
    location_link = models.CharField(max_length=256)
    image = models.CharField(max_length=256)

    meal = models.OneToOneField(Meal, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.meal.name}'

