from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from emailauth.serializer import FieldRenameTokenObtainPairSerializer
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
# Create your views here.


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = FieldRenameTokenObtainPairSerializer


logout_field = openapi.Parameter(
    'refresh_token', openapi.IN_QUERY, description="Enter refresh token", type=openapi.TYPE_STRING, required=True)


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(manual_parameters=[logout_field])
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
