from rest_framework import routers

from .views import PokemonsView
from .api import PokemonsViewSets
router = routers.DefaultRouter()

router.register('api/projects',PokemonsViewSets,'projects')
router.register('api/projects/vista', PokemonsView, 'vistaPokemon')
urlpatterns = router.urls