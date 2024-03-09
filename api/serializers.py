from rest_framework import serializers
from .models import models

class DragonBallSerializer(serializers.Serializer):
    id = serializers.IntegerField