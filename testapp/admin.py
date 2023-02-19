from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Model1)
class Model1(admin.ModelAdmin):
    list_display = [field.name for field in Model1._meta.fields]

@admin.register(Model2)
class Model2(admin.ModelAdmin):
    list_display = [field.name for field in Model2._meta.fields]
