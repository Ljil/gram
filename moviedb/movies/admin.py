from django.contrib import admin
from . import models

admin.site.register(models.Person)
admin.site.register(models.Movie)
admin.site.register(models.Genre)
admin.site.register(models.Gallery)
admin.site.register(models.Review)
