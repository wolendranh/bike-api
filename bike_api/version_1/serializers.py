from rest_framework import serializers
from models import Place, BicycleLine


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'description', 'work_time', 'updated_at', 'phone', 'address',
                  'name', 'home_page', 'created_at', 'longitude', 'latitude', 'type')


class BicycleLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BicycleLine
        fields = ("id", "line_path", "first_longitude", "street", "created_at",
                  "second_latitude", "updated_at", "second_longitude", "first_latitude")
