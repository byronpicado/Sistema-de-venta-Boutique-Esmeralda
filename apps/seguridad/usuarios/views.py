from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from yaml import serialize

from .Serializers import UserCreateSerializer
from drf_yasg.utils import swagger_auto_schema

class UserCreateView(APIView):
    @swagger_auto_schema(request_body=UserCreateSerializer)
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)

        # Validar datos
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Success"})

        # En caso de error, retornar las validaciones
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)