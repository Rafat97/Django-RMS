from django.contrib.auth.models import User, Group
from rest_framework import routers, serializers, viewsets


class EmployUserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4),
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        validated_data['is_staff'] = True
        employ_created = User.objects.create_user(**validated_data)
        my_group = Group.objects.get(name = 'Employ')
        print(my_group)
        my_group.user_set.add(employ_created) 
        print(employ_created)
        return employ_created
