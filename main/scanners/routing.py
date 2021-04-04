from django.urls import path

from .consumers import ScannerConsumer

websocket_urlpatterns = [
    path("scanners/ws/", ScannerConsumer.as_asgi())
]