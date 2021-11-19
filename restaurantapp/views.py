from django.db.models.query_utils import Q
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.decorators import permission_classes
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from django.http import HttpResponse
from drf_yasg import openapi
from .models import Restaurant, Item, Menu
from django.core.serializers import serialize
from .serializer import RestaurantSerializer, MenuSerializer, ItemSerializer


class RestaurantSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class MenuSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class ItemSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.DjangoModelPermissions]


restaurant = openapi.Parameter(
    'restaurant_id', openapi.IN_QUERY, description="Enter restaurant id", type=openapi.TYPE_INTEGER, required=True)


@swagger_auto_schema(methods=['GET'], manual_parameters=[restaurant, ],)
@api_view(['GET'])
@permission_classes([permissions.DjangoModelPermissions])
def get_restaurant_menu(request, format=None):
    content = {}
    rest_id = request.GET['restaurant_id']

    serializer = RestaurantSerializer(Restaurant.objects.get(id=rest_id))
    content["restaurant"] = serializer.data
    get_object = Menu.objects.filter(
        restaurant__pk=rest_id, is_active__exact=True).get()
    current_active_menu = MenuSerializer(get_object)
    content["menu"] = current_active_menu.data
    menuId = get_object.id
    print(menuId)
    get_object = Item.objects.filter(menu__pk=menuId, is_available=True)
    print(get_object)
    current_active_items = ItemSerializer(get_object, many=True)
    content["items"] = current_active_items.data

    return Response(content)
    return HttpResponse({}, content_type='application/json')
