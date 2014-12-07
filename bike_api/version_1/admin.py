from django.contrib import admin
from bike_api.version_1.models import Place


class PlaceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Place, PlaceAdmin)