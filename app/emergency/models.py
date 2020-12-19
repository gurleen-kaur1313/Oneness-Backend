from django.conf import settings
from django.db import models
import uuid


class Emergency(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    longitude = models.CharField(null=True, blank=True, max_length=250)
    latitude = models.CharField(null=True, blank=True, max_length=250)
    date = models.CharField(null=True, blank=True, max_length=250)

    def __str__(self):
        return self.user.name

    def save(self, *args, **kwargs):
        super(Emergency, self).save(*args, **kwargs)
