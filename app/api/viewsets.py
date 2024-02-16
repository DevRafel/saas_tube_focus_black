from rest_framework import viewsets
from app.api import serializers
from app import models

class AppViewSet(viewsets.ModelViewSet):
       serializer_class = serializers.AppSerializer
       queryset = models.App.objects.all()