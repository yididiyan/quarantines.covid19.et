from rest_framework import serializers

from covid19_quarantine.quarantine.models import QuarantineCenter


class QuarantineCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarantineCenter
        fields = ['name', 'location', 'address', 'admin', 'capacity', 'occupied_units']


