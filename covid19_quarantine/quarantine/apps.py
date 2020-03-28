from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class QuarantineConfig(AppConfig):
    name = 'covid19_quarantine.quarantine'
    verbose_name= _("Quarantine Centers")
