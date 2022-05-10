from rest_framework import serializers

from app.models import Ai1, Ai2


class Ai1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ai1
        fields = '__all__'


class Ai2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ai2
        fields = '__all__'
