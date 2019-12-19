from django.db import models
from mdrm.mdrm import MDRMModel
from mdrm.models import Ingredient


class Meal(MDRMModel):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    serve_start = models.DateField()
    serve_end = models.DateField()

    recipes = models.ManyToManyField('Recipe', related_name='meals', blank=True, null=True) #todo:// remove blank=True

    def __str__(self):
        return self.name


class Recipe(MDRMModel):
    name = models.CharField(max_length=200)

    ingredients = models.ManyToManyField('RecipeIngredient', related_name='recipes')

    def __str__(self):
        return self.name


class RecipeIngredient(MDRMModel):
    OZ = 1
    FLOZ = 2
    EA = 3

    UNITS = (
        (OZ, 'oz'),
        (FLOZ, 'fl oz'),
        (EA, 'ea'),
    )

    quantity = models.FloatField(default=0)
    unit = models.SmallIntegerField(choices=UNITS, default=OZ)
    ingredient = models.ManyToManyField(Ingredient)

    def __str__(self):
        return f'{self.quantity}{dict(self.UNITS)[self.unit]} {self.ingredient.name}'