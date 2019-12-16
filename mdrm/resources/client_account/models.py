from django.db import models
from mdrm.mdrm import MDRMModel
from mdrm.models import Allergen
from mdrm.resources.client_account.managers import ProfileManager


class Profile(MDRMModel):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=25)

    allergens = models.ManyToManyField(Allergen, related_name='profiles')
    object = ProfileManager()