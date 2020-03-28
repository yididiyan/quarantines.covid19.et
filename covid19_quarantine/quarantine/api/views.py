from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import QuarantineCenterSerializer
from covid19_quarantine.quarantine.models import QuarantineCenter


class QuarantineCenterViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = QuarantineCenterSerializer
    queryset = QuarantineCenter.objects.all()

    def get_queryset(self, *args, **kwargs):
        return self.queryset


