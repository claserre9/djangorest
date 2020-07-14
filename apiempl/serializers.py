from rest_framework import serializers
from apiempl import models


class UserSerializer(serializers.ModelSerializer):
    """Serialize a user object"""

    class Meta:
        model = models.User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'password', 'birthday', 'phone', 'country', 'city', 'profession',
            'is_licenced', 'date_joined')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input-type': 'password'}
            }
        }

    def create(self, validated_data):
        '''Create a new user'''
        user = models.User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
            birthday=validated_data['birthday'],
            phone=validated_data['phone'],
            country=validated_data['country'],
            city=validated_data['city'],
            profession=validated_data['profession'],
            is_licenced=validated_data['is_licenced'],
        )
        return user

class UserCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserComment
        fields = '__all__'

class UserForumPostSerializer(serializers.ModelSerializer):
    """Serialize a user forum post"""
    comments = UserCommentSerializer(many=True, read_only=True)

    class Meta:
        model = models.UserForumPost
        fields = ('id', 'user', 'title', 'content', 'comments' ,'category', 'created', 'modified')
        extra_kwargs = {'user': {'read_only': True}}
