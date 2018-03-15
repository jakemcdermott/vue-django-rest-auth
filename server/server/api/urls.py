from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    PostViewSet,
)

router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = router.urls
