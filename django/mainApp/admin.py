from django.contrib import admin
from mainApp import models

# Register your models here.

# form model
admin.site.register(models.TodolistForm)
# blog model
admin.site.register(models.Blog)