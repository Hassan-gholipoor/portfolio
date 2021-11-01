from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Personal)
admin.site.register(models.Category)
admin.site.register(models.Skills)
admin.site.register(models.Education)
admin.site.register(models.Experience)
admin.site.register(models.SocialMedia)