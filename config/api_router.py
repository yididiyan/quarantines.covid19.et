from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from covid19_quarantine.users.api.views import UserViewSet
from covid19_quarantine.quarantine.api.views import QuarantineCenterViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("quarantine", QuarantineCenterViewSet)


app_name = "api"
urlpatterns = router.urls
