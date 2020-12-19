from django.db import models
import uuid
from django.conf import settings


class NGO(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    ngo_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(NGO, self).save(*args, **kwargs)
