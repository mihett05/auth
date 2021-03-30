from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RetrieveAccountView, CreateAccountView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("create/", CreateAccountView.as_view(), name="create_account"),
    path("", RetrieveAccountView.as_view(), name="retrieve_account")
]

