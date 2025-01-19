from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ShortenedURL, AccessLog

# Register the models
@admin.register(ShortenedURL)
class ShortenedURLAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_url', 'created_at', 'expires_at','access_count')
    search_fields = ('original_url', 'short_url')
    list_filter = ('created_at', 'expires_at')

@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('shortened_url', 'timestamp', 'ip_address')
    search_fields = ('shortened_url__short_url',)
    list_filter = ('timestamp',)
