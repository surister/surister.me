from rest_framework.routers import DefaultRouter

from .views import PostMetaView

router = DefaultRouter()
router.register(r'post', PostMetaView, basename='post-meta')
urlpatterns = router.urls
