from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response
from rest_framework.generics import CreateAPIView

from .models import Scanner
from .serializers import ScannerSerializer, TokenSerializer
from .signals import command_open


class CreateScanner(CreateAPIView):
    queryset = Scanner.objects.all()
    serializer_class = ScannerSerializer

    permission_classes = [AllowAny]


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

