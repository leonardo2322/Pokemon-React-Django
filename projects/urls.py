from rest_framework import routers
from .api import PokemonsViewSets
router = routers.DefaultRouter()

router.register('api/projects',PokemonsViewSets,'projects')

urlpatterns = router.urls