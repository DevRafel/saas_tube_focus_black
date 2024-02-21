from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from app.api import viewsets as pastaviewsets

route = routers.DefaultRouter()

route.register(r'api', pastaviewsets.PastaViewSet, basename="api" )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
