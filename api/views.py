from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import GeoLocation
from .permissions import IsUserOrReadOnly
from .serializers import CreateGeoLocationSerializer, GeoLocationSerializer


class GeoLocationViewSet(
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrives user accounts
    """
    queryset = GeoLocation.objects.all()
    serializer_class = GeoLocationSerializer
    permission_classes = (IsUserOrReadOnly,)

    def get_urls(self):
        """
        Return a list of URL patterns, given the registered viewsets.
        """
        raise NotImplementedError('get_urls must be overridden')

class GeoLocationCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = GeoLocation.objects.all()
    serializer_class = CreateGeoLocationSerializer
    permission_classes = (AllowAny,)
    def get_urls(self):
        """
        Return a list of URL patterns, given the registered viewsets.
        """
        raise NotImplementedError('get_urls must be overridden')
