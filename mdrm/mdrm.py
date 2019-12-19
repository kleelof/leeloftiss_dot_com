from django.db import models


class MDRMModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MDRMResource:
    pass