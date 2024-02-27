from rest_framework import serializers
from app import models
from app.models import Pasta, SubPasta
from app.models import BoardApp

class PastaSerializer(serializers.ModelSerializer):
       class Meta:
              model = models.Pasta
              fields = '__all__'
              
                                   
class SubPastaSerializer(serializers.ModelSerializer):  
       class Meta:
              model = SubPasta
              fields = '__all__'
              
              
class BoardAppSerializer(serializers.ModelSerializer):
       
       class Meta:
              model = BoardApp
              fields = '__all__'