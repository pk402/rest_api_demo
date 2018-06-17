from datetime import datetime
import jsonfield
import json
import urllib
import requests

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import ValidationError
from .geo_location import GeoLocationApi

class GeoLocationManager(models.Manager):
    def create_address(self, latitude, longitude):
        print(self, latitude, longitude)
        try:
            return self.get(latitude=latitude,longitude=longitude)
        except self.model.DoesNotExist:
            pass

        location = self.model(latitude=latitude,longitude=longitude)
        location.create_address(save=True)
        print(self, latitude, longitude,location)
        return location

class GeoLocation(models.Model):

    created = models.DateTimeField(
        _('created'), default=datetime.now, db_index=True)
    _data = jsonfield.JSONField(editable=False, blank=True, null=True)
    formatted_address = models.TextField(_('formatted address'), blank=True)
    latitude = models.DecimalField(
        _('latitude'), max_digits=20, decimal_places=9,
        blank=True, null=True)
    longitude = models.DecimalField(
        _('longitude'), max_digits=20, decimal_places=9,
        blank=True, null=True)

    objects = GeoLocationManager()

    class Meta:
        verbose_name = _('geolocation')
        verbose_name_plural = _('geolocations')

    def __unicode__(self):
        if self.latitude is None or self.longitude is None:
            return u'%s (failed)' % self.address
        return self.address

    def create_address(self, save=False):
        location_obj = GeoLocationApi(settings.GEOLOCATION_KEY)
        response = location_obj.get_location(self.latitude,self.longitude)
        error_message = response.get('error_message')
        if error_message:
            print(response)
            raise ValidationError('%s Please contact site admin.'%error_message)

        try:
            results = response['results'][0]  # use first result
            location = results['geometry']['location']

            self.formatted_address = results['formatted_address']
            self.latitude = location['lat']
            self.longitude = location['lng']
        except IndexError as e:
            raise ValidationError('Result not received. Please contact site admin.')
            self.formatted_address = u'geocoding failed'
            self.latitude = None
            self.longitude = None

        if save:
            self._data = response
            self.save()

    def is_valid(self):
        return self.latitude is not None and self.longitude is not None
