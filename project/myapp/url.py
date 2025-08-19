from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'project')    

urlpatterns = router.urls
# Este archivo define las URLs para la API del proyecto.