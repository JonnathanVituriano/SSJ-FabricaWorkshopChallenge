from django.urls import path

from api_rest.views import PokemonsViewSet, pokemon_detalhes, pokemon_detalhes_especifico

urlpatterns = [
    path('api/v1/pokemons/', PokemonsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/pokemons/<int:pk>/', PokemonsViewSet.as_view({'get': 'retrieve'})),
    path('pokemon/', pokemon_detalhes, name="pokemon_detalhes"),
    path('pokemon/<str:nome>/', pokemon_detalhes_especifico, name="pokemon_detalhes_especifico"),
]
