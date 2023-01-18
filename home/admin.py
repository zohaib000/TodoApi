from django.contrib import admin
from .models import *
# Register your models here.
MODELS=[Todo]

for MODEL in MODELS:
    @admin.register(MODEL)
    class AdminModel(admin.ModelAdmin):
        list_display=[field.name for field in MODEL._meta.get_fields()]