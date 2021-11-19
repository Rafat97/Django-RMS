from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets
from .models import Vote
from restaurantapp.models import Menu


class VotingSerializer(serializers.Serializer):

    vote_type = serializers.IntegerField()
    restaurant = serializers.IntegerField()
    user = serializers.IntegerField()

    def validate(self, attrs):
        print(attrs)
        restaurant_menu = attrs.get('restaurant', '')
        user_id = attrs.get('user', '')
        if not Menu.objects.filter(pk=restaurant_menu).exists():
            raise serializers.ValidationError(
                {'error': ('Restaurant\'s Menu does not exist')})

        if Vote.objects.filter(restaurant_menu__pk=restaurant_menu, User__pk=user_id).exists():
            raise serializers.ValidationError(
                {'error': ('You already gave review')})

        return super().validate(attrs)

    def create(self, validated_data):
        current_resturent = Menu.objects.get(pk=validated_data['restaurant'])
        current_user = User.objects.get(pk=validated_data['user'])
        employ_created = Vote.objects.create(
            User=current_user, restaurant_menu=current_resturent, vote_type=validated_data['vote_type'])
        return employ_created
