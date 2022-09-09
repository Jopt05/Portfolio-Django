from rest_framework import serializers


class SendEmailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=255)
