import jwt
from django.conf import settings
from rest_framework import serializers

from .models import Scanner


class ScannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scanner
        fields = ["username"]
        read_only_fields = ["id"]
        write_only_fields = ["password"]


class Token:
    def __init__(self, token: str):
        self.token = token
        self.payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(required=True)

    def create(self, validated_data):
        return Token(validated_data["token"])

    def update(self, instance, validated_data):
        return self.create(validated_data)
