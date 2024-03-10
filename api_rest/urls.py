from rest_framework.routers import DefaultRouter
from django.urls import path, include
from api_rest.views import PokemonsViewSet
from django.contrib import admin

router = DefaultRouter()

router.register("nome", PokemonsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]