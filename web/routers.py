from rest_framework.routers import DefaultRouter
from .users.views import UserViewSet, UserCreateViewSet
from api.views import GeoLocationViewSet, GeoLocationCreateViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'user/new', UserCreateViewSet, base_name='user/new')

router.register(r'locations', GeoLocationViewSet, base_name='locations')
router.register(r'location/new', GeoLocationCreateViewSet, base_name='location/new')
