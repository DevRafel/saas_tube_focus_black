from rest_framework import serializers
from app import models
from app.models import Pasta, SubPasta

class PastaSerializer(serializers.ModelSerializer):
       class Meta:
              model = models.Pasta
              fields = '__all__'
              
                                   
class SubPastaSerializer(serializers.ModelSerializer):  
       class Meta:
              model = SubPasta
              fields = '__all__'