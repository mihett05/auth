from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response

from .models import Scanner
from .serializers import ScannerSerializer, TokenSerializer
from .signals import command_open


class CreateScanner(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ScannerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        scanner = serializer.save()
        scanner.set_password(serializer.validated_data["password"])
        scanner.save()

        return Response(dict(), status=201)


class ScanToken(APIView):
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()

        if "uuid" in token.payload and token.payload["uuid"]:
            command_open.send(
                self.__class__,
                uuid=token.payload["uuid"],
                user_id=request.user.pk
            )
        else:
            return Response({
                "error": "invalid token"
            }, status=400)

