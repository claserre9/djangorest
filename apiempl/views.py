from django.shortcuts import render
from rest_framework import viewsets, filters
from apiempl import models, serializers, permissions
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    """Create and update a user"""
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('last_name', 'email',)
