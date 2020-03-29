from rest_framework import serializers

from covid19_quarantine.quarantine.models import QuarantineCenter


class QuarantineCenterSerializer(serializers.HyperlinkedModelSerializer):
    admin = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='api:user-detail',
        lookup_field='username'
    )

    class Meta:
        model = QuarantineCenter
        fields = ['url', 'id', 'name', 'location', 'address', 'admin', 'capacity', 'occupied_units']

        extra_kwargs = {
            'url': {'view_name': 'api:quarantinecenter-detail', 'lookup_field': 'pk'}
        }

