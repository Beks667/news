from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, NewsViewSet

router = DefaultRouter()
router.register('category',CategoryViewSet,basename='category')
router.register('news',NewsViewSet,basename='news')

urlpatterns = router.urls
