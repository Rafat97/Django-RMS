from django.contrib.auth.models import User, Group
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class FieldRenameTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD
