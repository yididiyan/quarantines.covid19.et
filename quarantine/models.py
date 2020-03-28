from django.db import models
from django.contrib.gis.db import models as gis_models
from covid19_quarantine.users.models import User

class QuarantineCenter(models.Model):
    name = models.CharField("Name of the center", blank=False, max_length=255)
    location = gis_models.PointField()
    address = models.CharField(max_length=255)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField(help_text="Total number of ICUs in the quarantine")
    occupied_units = models.IntegerField(help_text="Number of currently occupied ICUs")