from rest_framework import serializers
from app import models

class PastaSerializer(serializers.ModelSerializer):
       class Meta:
              model = models.Pasta
              fields = '__all__'