from django.shortcuts import redirect, render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Pokemons
from .serializers import PokemonsSerializers

import requests

class PokemonsViewSet(ModelViewSet):

    queryset = Pokemons.objects.all()
    serializer_class = PokemonsSerializers

    def retrieve(self, request, pk=None):
        try:
            pokemon = get_object_or_404(Pokemons, id=pk)
            serializer = PokemonsSerializers(pokemon)
            return Response(serializer.data)
        except Pokemons.DoesNotExist:
            return Response(status=404, data={'error': 'Pokemon não encontrado'})

    
    def create(self, request):


        nome = request.data.get('name')
        site = 'https://pokeapi.co/api/v2/pokemon/{nome}/.json'

        requisicao = request.get(site)

        json = requisicao.json()

        nome = json.get('nome', '')
        height = json.get('altura','')
        weight = json.get('peso','')
        tipo_pokemon = json.get('tipo','')
        
        dados_recebidos = {
            'nome': f'{nome}',
            'height': f'{height}',
            'weight': f'{weight}',
            'tipo_pokemon': f'{tipo_pokemon}', 
        }
        
        meuserializer = PokemonsSerializers(data= dados_recebidos)

        if meuserializer.is_valid():

            pokemon_pesquisado = Pokemons.objects()

            pokemon_pesquisado_existe = pokemon_pesquisado.exists()

            if pokemon_pesquisado_existe:

                meuserializer.save()
                return meuserializer
            else:
                return Response('Pokemon não existe')

def pokemon_detalhes(request):

    if request.method == 'POST':
        nome_pokemon = request.POST.get("nome_pokemon")
        return redirect("pokemon_detalhes_especifico", nome=nome_pokemon)
    else:
        return render(request, "pokemon_search_form.html")

def pokemon_detalhes_especifico(request, nome):

    try:
        resposta_api = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome}")
        resposta_api.raise_for_status()

        dados_pokemon = resposta_api.json()
        return render(request, "pokemon_detalhes.html", {"pokemon": dados_pokemon})
    except requests.exceptions.RequestException as err:
        return render(request, "erro.html", {"mensagem": f"Erro ao buscar dados do Pokemon: {err.args[0]}"})

