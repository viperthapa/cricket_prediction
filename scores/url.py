from django.urls import include, path
from .views import app1, SituationViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Situation', SituationViewSet)

# urlpatterns = re_path('', url(r'^home/', 'scores.views.app1', name = 'app1'),)

app_name = 'scores'
urlpatterns = [
    path('form/', app1, name='app1'),

    # path('add', add, name='add'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
