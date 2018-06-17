from django.contrib import admin

from .models import GeoLocation


admin.site.register(
    GeoLocation,
    list_display=(
        'id', 'created', 'latitude', 'longitude'),
    search_fields=('formatted_address',),
)
