from django.db import models
from django.conf import settings
from django.utils import timezone
from protestId.models import Protest
import uuid


class Donation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True)
    made_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    transactionId = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    made_to = models.ForeignKey(Protest, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.made_by.name

    def save(self, *args, **kwargs):
        super(Donation, self).save(*args, **kwargs)

