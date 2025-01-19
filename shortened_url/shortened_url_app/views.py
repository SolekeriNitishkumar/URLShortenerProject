# shortener/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from django.utils.timezone import now
from .models import ShortenedURL, AccessLog
from .serializers import ShortenedURLSerializer, CreateShortenedURLSerializer
import datetime

class ShortenURLView(APIView):
    def post(self, request):
        serializer = CreateShortenedURLSerializer(data=request.data)
        if serializer.is_valid():
            original_url = serializer.validated_data['original_url']
            expires_in_hours = serializer.validated_data['expires_in_hours']
            expires_at = now() + datetime.timedelta(hours=expires_in_hours)

            short_url, created = ShortenedURL.objects.get_or_create(
                original_url=original_url,
                defaults={'expires_at': expires_at}
            )
            return Response(ShortenedURLSerializer(short_url).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RedirectView(APIView):
    def get(self, request, short_url):
        url = get_object_or_404(ShortenedURL, short_url=short_url)
        if url.expires_at < now():
            return Response({"error": "URL has expired."}, status=status.HTTP_410_GONE)
        
        # Log the access
        AccessLog.objects.create(shortened_url=url, ip_address=request.META.get('REMOTE_ADDR'))
        url.access_count += 1
        url.save()

        return redirect(url.original_url)

class AccessLogAnalyticsView(APIView):
    def get(self, request, short_url):
        url = get_object_or_404(ShortenedURL, short_url=short_url)
        logs = AccessLog.objects.filter(shortened_url=url).values('timestamp', 'ip_address')
        return Response({
            "original_url": url.original_url,
            "short_url": url.short_url,
            "access_count": url.access_count,
            "access_logs": list(logs),
        })
