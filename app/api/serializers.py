from rest_framework import serializers
from app import models

class AppSerializer(serializers.ModelSerializer):
       class Meta:
              model = models.App
              fields = '__all__'