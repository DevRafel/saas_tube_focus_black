from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from app.api import viewsets as pastaviewsets
from app.api import viewsets as subpastaviewsets

router = routers.DefaultRouter()

router.register(r'pasta', pastaviewsets.PastaViewSet, basename="pasta" )
router.register(r'subpasta', subpastaviewsets.SubPastaViewSet, basename='subpasta' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
