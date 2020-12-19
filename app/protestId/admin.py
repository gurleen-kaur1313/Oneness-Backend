from protestId.models import Protest
from django.contrib import admin
from .models import Protest,Calendar

admin.site.register(Protest)
admin.site.register(Calendar)
