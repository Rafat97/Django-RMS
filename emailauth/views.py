from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from emailauth.serializer import FieldRenameTokenObtainPairSerializer

# Create your views here.


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = FieldRenameTokenObtainPairSerializer
