from protestId.models import Protest
from django.db import models
import uuid


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    locality = models.CharField(
        blank=True, null=True, max_length=255)
    city = models.CharField(
        blank=True, null=True, max_length=255)
    state = models.CharField(
        blank=True, null=True, max_length=255)
    protest = models.ForeignKey(Protest, on_delete=models.CASCADE)

    def __str__(self):
        return self.protest.title

    def save(self, *args, **kwargs):
        super(Location, self).save(*args, **kwargs)

