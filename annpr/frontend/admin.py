from django.contrib import admin

# Register your models here.
from .models import NumberPlate,MediaFiles
admin.site.register(NumberPlate)
admin.site.register(MediaFiles)
