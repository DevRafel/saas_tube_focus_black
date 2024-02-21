from rest_framework import viewsets
from app.api import serializers
from app import models

class PastaViewSet(viewsets.ModelViewSet):
       serializer_class = serializers.PastaSerializer
       queryset = models.Pasta.objects.all()