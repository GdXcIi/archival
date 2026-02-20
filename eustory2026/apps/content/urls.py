from rest_framework.routers import DefaultRouter
from .views import ContentBlockViewSet, SourceViewSet

router = DefaultRouter()
router.register(r'content', ContentBlockViewSet, basename='content')
router.register(r'sources', SourceViewSet, basename='sources')

urlpatterns = router.urls