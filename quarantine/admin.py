from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import QuarantineCenter


@admin.register(QuarantineCenter)
class QuarantineCenterAdmin(OSMGeoAdmin):
    list_display = ('name', 'location', 'address', 'capacity', 'occupied_units')