from django.shortcuts import render
from rest_framework import viewsets
from apiempl import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    """Create and update a user"""
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

