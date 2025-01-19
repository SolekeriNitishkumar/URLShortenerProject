from django.urls import path
from . import views

urlpatterns = [
    path('shorten', views.ShortenURLView.as_view(), name='shortened_url'),
    path('<str:short_url>', views.RedirectView.as_view(), name='redirect_to_orginal_url'),
    path('analytics/<str:short_url>', views.AccessLogAnalyticsView.as_view(), name='AccessLog'),
]

