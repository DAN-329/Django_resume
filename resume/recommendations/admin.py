from django.contrib import admin

# Register your models here.
from recommendations import models


admin.site.register(models.Record)
admin.site.register(models.Test)