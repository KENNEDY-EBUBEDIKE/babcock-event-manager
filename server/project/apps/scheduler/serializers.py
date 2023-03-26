from rest_framework.serializers import ModelSerializer
from .models import *


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class VenueSerializer(ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'
