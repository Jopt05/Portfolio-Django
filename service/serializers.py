from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    """ Serializer de servicios """

    class Meta:
        model = Service
        fields = (
            'service_name',
            'service_description',
            'service_topic',
            'service_image',
        )
