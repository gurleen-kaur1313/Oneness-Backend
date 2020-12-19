from django.db import models
import uuid
from django.conf import settings


class Protest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        unique=True, blank=True, null=True, max_length=255)
    participants = models.IntegerField(default=0, null=True, blank=True)
    leaders = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    upiId = models.CharField(null=True, blank=True, max_length=255)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Protest, self).save(*args, **kwargs)


class Calendar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        unique=True, blank=True, null=True, max_length=255)
    day = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    protest = models.ForeignKey(Protest, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Calendar, self).save(*args, **kwargs)
