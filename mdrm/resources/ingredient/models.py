from django.db import models
from mdrm.mdrm import MDRMModel


class Allergen(MDRMModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ingredient(MDRMModel):
    name = models.CharField(max_length=200)

    allergens = models.ManyToManyField(Allergen, related_name='ingredients', blank=True)

    def __str__(self):
        return self.name
