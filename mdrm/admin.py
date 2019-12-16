from django.contrib import admin

from mdrm.models import *

admin.site.register(Profile)
admin.site.register(Allergen)
admin.site.register(Ingredient)
admin.site.register(Meal)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(DeliveryWindow)
admin.site.register(Order)
