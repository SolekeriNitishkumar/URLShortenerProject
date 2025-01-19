# shortener/serializers.py
from rest_framework import serializers
from .models import ShortenedURL

class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = '__all__'

class CreateShortenedURLSerializer(serializers.Serializer):
    original_url = serializers.URLField()
    expires_in_hours = serializers.IntegerField(default=24)
