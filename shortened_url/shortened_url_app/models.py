from django.db import models
from hashlib import md5
import datetime


# Create your models here.

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    access_count = models.IntegerField(default=0)

    def save(self,*args,**kwargs):
        if not self.short_url:
            self.short_url = md5(self.original_url.encode()).hexdigest()[:6]
            print(self.short_url)
        super().save(*args, **kwargs)

class AccessLog(models.Model):
    shortened_url = models.ForeignKey(ShortenedURL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()


        
