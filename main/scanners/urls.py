from django.urls import path

from .views import CreateScanner, ScanToken

urlpatterns = [
    path("create/", CreateScanner.as_view()),
    path("scan/", ScanToken.as_view())
]
