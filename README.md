# SSJ-FabricaWorkshopChallenge
Projeto API Pokemon
Descrição:

Este projeto implementa uma API RESTful para Pokemons, permitindo a busca e criação de Pokemons. A API utiliza a API externa PokeAPI para obter dados dos Pokemons.

Funcionalidades:

GET /api/v1/pokemons: Retorna uma lista de Pokemons.
GET /api/v1/pokemons/<int:pk>: Retorna os detalhes de um Pokemon específico.
POST /api/v1/pokemons: Cria um novo Pokemon.
Tecnologias:

Django
Django REST Framework
Python
API PokeAPI
Exemplo de uso:

Para obter a lista de Pokemons:
curl -X GET http://localhost:8000/api/v1/pokemons/
Para obter os detalhes de um Pokemon específico:
curl -X GET http://localhost:8000/api/v1/pokemons/1/
Para criar um novo Pokemon:
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"nome": "Bulbasaur"}' \
    http://localhost:8000/api/v1/pokemons/
Observações:

Este projeto é um exemplo básico e pode ser adaptado de acordo com suas necessidades.
Consulte a documentação da API PokeAPI para obter mais informações sobre os dados dos Pokemons.
Certifique-se de ter o Django e o Python instalados em seu ambiente.
Como executar:

Clone este repositório para o seu computador.
Crie um ambiente virtual Python e ative-o.
Instale as dependências do projeto:
pip install -r requirements.txt
Execute o servidor Django:
python manage.py runserver
Acesse a API no seu navegador:
http://localhost:8000/api/v1/pokemons/