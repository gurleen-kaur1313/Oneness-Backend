from django.db import models
import uuid
from protestId.models import Protest


class ResoucesRequired(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(null=True, blank=True,
                             unique=True, max_length=255)
    quantity = models.CharField(null=True, blank=True, max_length=255)
    protest = models.ForeignKey(Protest, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(ResoucesRequired, self).save(*args, **kwargs)

