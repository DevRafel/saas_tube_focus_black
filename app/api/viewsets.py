from rest_framework import viewsets
from app.api import serializers
from app import models
from app.models import SubPasta
from app.models import BoardApp
from app.api.serializers import BoardAppSerializer
from app.api.serializers import SubPastaSerializer

class PastaViewSet(viewsets.ModelViewSet):
       serializer_class = serializers.PastaSerializer
       queryset = models.Pasta.objects.all()
       
       
       
class SubPastaViewSet(viewsets.ModelViewSet):
       serializer_class = SubPastaSerializer
       queryset = SubPasta.objects.all()
       
       
class BoardAppViewSet(viewsets.ModelViewSet):
       serializer_class = BoardAppSerializer
       queryset = BoardApp.objects.all()