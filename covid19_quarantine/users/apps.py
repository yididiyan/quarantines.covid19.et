from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "covid19_quarantine.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import covid19_quarantine.users.signals  # noqa F401
        except ImportError:
            pass
