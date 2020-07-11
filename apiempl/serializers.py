from rest_framework import serializers
from apiempl import models


class UserSerializer(serializers.ModelSerializer):
    """Serialize a user object"""

    class Meta:
        model = models.User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'password', 'phone', 'country', 'city', 'profession',
            'is_licenced')
        extra_kwargs ={
            'password':{
                'write_only': True,
                'style':{'input-type':'password'}
            }
        }
    def create(self, validated_data):
        '''Create a new user'''
        user = models.User.objects.create_user(
            email=validated_data['email'],
            first_name= validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )

        return user