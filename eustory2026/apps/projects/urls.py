from rest_framework.routers import DefaultRouter
from .views import SubThemeViewSet

router = DefaultRouter()
router.register(r'subthemes', SubThemeViewSet)

urlpatterns = router.urls