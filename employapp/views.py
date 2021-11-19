from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from .serializer import EmployUserSerializer
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from drf_yasg import openapi
# Create your views here.


# class CustomAPIView(APIView):
#     def get_permissions(self):
#         # Instances and returns the dict of permissions that the view requires.
#         return {key: [permission() for permission in permissions] for key, permissions in self.permission_classes.items()}

#     def check_permissions(self, request):
#         # Gets the request method and the permissions dict, and checks the permissions defined in the key matching
#         # the method.
#         method = request.method.lower()
#         for permission in self.get_permissions()[method]:
#             if not permission.has_permission(request, self):
#                 self.permission_denied(
#                     request, message=getattr(permission, 'message', None)
#                 )


# class EmployApiView(CustomAPIView):

#     serializer_class = EmployUserSerializer
#     permission_classes = {"get": [permissions.AllowAny], }

#     def get(self, request, format=None):
#         # snippets = EmployUserSerializer.objects.all()
#         # serializer = self.serializer_class(data=request.data)
#         print("sad")

#         return Response("sadas", status=status.HTTP_204_NO_CONTENT)


# email_param = openapi.Parameter(
#     'Email', openapi.IN_QUERY, description="Enter email address", type=openapi.TYPE_STRING)
# password_param = openapi.Parameter(
#     'Password', openapi.IN_QUERY, description="Enter password", type=openapi.TYPE_STRING)

# password_param = openapi.Parameter(
#     'Password', openapi.IN_QUERY, description="Enter password", type=openapi.TYPE_STRING)

# @swagger_auto_schema(methods=['POST'], manual_parameters=[email_param,password_param],)
# @api_view(['POST'])
# @permission_classes([permissions.AllowAny])
# def add_employ(request, format=None):
#     content = {
#         'status': 'request was permitted'
#     }
#     print(request.POST)
#     # user = User.objects.create_user(email='myemail@crazymail.com', username='myemail@crazymail.com', password='mypassword', is_staff=True)
#     return Response(content)

class EmployAddView(GenericAPIView):
    serializer_class = EmployUserSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = EmployUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)