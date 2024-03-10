from django.db import models

class Pokemons(models.Model):
    name = models.CharField(verbose_name = 'nome: ', max_length = 100)
    height = models.IntegerField(verbose_name = 'altura: ')
    weight = models.IntegerField(verbose_name = 'peso: ')
    tipo_pokemon = models.CharField(verbose_name = 'tipo do pokemon: ', max_length = 30)


    def __str__(self):
        return f'nome do pokemon: {self.name} altura do pokemon: {self.height} peso do pokemon: {self.weight} tipo do pokemon: {self.tipo_pokemon}'
     