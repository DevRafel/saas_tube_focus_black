from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from app.api import viewsets as pastaviewsets
from app.api import viewsets as subpastaviewsets
from app.api import viewsets as boardappviewsets

router = routers.DefaultRouter()

router.register(r'pasta', pastaviewsets.PastaViewSet, basename="pasta" )
router.register(r'subpasta', subpastaviewsets.SubPastaViewSet, basename='subpasta' )
router.register(r'boardapp', boardappviewsets.BoardAppViewSet, basename='boardapp' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
