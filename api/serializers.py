from rest_framework import serializers
from .models import GeoLocation


class GeoLocationSerializer(serializers.ModelSerializer):
    # location_address = serializers.SerializerMethodField()
    class Meta:
        model = GeoLocation
        fields = ('id', 'latitude', 'longitude', 'formatted_address',)
    def get_location_address(self, obj):
        return "Foo id: %r" % obj.address


class CreateGeoLocationSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        location = GeoLocation.objects.create_address(**validated_data)
        return location

    class Meta:
        model = GeoLocation
        fields = ('id', 'latitude', 'longitude',)
        read_only_fields = ('formatted_address',)
        # extra_kwargs = {
        #     'formatted_address': {'write_only': True},
        #     'latitude': {'max_digits': 16, 'decimal_places': 2}
        # }
