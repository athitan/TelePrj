from rest_framework import routers
from App.models import prepaid,postpaids
from App.viewsets import prepaidViewSet,postpaidsiewSet
router = routers.DefaultRouter()
router.register('prepaid',prepaidViewSet)
router.register('postpaids',postpaidsiewSet)