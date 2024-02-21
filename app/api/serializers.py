from rest_framework import serializers
from app.models import Pasta, SubPasta

class PastaSerializer(serializers.ModelSerializer):
       class Meta:
              model = Pasta
              fields = '__all__'
              
              
class SubPastaSerializer(serializers.ModelSerializer):
       class Meta:
              model = SubPasta
              fields = '__all__'