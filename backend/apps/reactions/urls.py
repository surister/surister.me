from rest_framework.routers import DefaultRouter

from .views import PostMetaView, PostMetaView2

router = DefaultRouter()
router.register(r'post', PostMetaView, basename='post-meta')
router.register(r'post2', PostMetaView2, basename='whatever')
urlpatterns = router.urls
