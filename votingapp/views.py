from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import status, permissions
from rest_framework.response import Response
from .serializer import VotingSerializer
from .models import Vote
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# {
#   "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNzM3MjMxMiwiaWF0IjoxNjM3Mjg1OTEyLCJqdGkiOiJmOTQyMTQyNjkxNzQ0MzEyODhhMzhmMDBkMDBiZGIzMSIsInVzZXJfaWQiOjJ9.y135p0tgY0RyFEhHjayPUzFk8dGtl2bz4wG7ofABxoY",
#   "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3Mjg5NTEyLCJpYXQiOjE2MzcyODU5MTIsImp0aSI6IjkyN2ZjNzNkYjY5OTRiOTM5Zjg2Njg5ZjI0Y2VhOGUxIiwidXNlcl9pZCI6Mn0.cfpzSz5XKlgr5bCl1oupk6RxiG8cJtKjYbD83PzvIjA"
# }


# class OnlyProvidersPermission(permissions.BasePermission):
#     message = 'Only Providers are allowed to access.'

#     def has_permission(self, request, view):
#         return request.user.is_authenticated and (
#             request.user.is_provider() or request.user.is_superuser)

class VoteAddView(GenericAPIView):
    serializer_class = VotingSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def get_queryset(self):
        return Vote.objects.all()
    
    def post(self, request):
        request.data['user'] = request.user.id

        print(request.data)
        
        serializer = VotingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
