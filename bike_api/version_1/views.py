from models import Place, BicycleLine
from serializers import PlaceSerializer, BicycleLineSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PlacesList(APIView):
    """
    List all places
    """
    def get(self, request, format=None):
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlaceSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BicycleLinesList(APIView):
    """
    List all Bicycle Routes
    """
    def get(self, request, format=None):
        routes = BicycleLine.objects.all()
        serializer = BicycleLineSerializer(routes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BicycleLineSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)