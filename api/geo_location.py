import os
import requests

class GeoLocationApi(object):

    GEOLOCATION_URL = "https://maps.googleapis.com/maps/api/geocode/json"

    def __init__(self,key):
        self.key = key
        self.session = requests.Session()

    def get_params(self,latitude,longitude):
        return {
        'key':self.key,
        'sensor': 'false',
        'latlng': '%s,%s'%(latitude,longitude),
        }

    def get_location(self,latitude=28.6493845,longitude=77.3520734):
        params = self.get_params(latitude,longitude)
        response = self.session.get(self.GEOLOCATION_URL, params=params)
        return response.json()

if __name__ == '__main__':
    location_obj = GeoLocationApi(key='demo')
    print(location_obj.get_location())
