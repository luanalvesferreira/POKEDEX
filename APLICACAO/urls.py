from django.contrib import admin
from django.urls import path
from .views import *

app_name="APLICACAO"

urlpatterns = [
    path("listar", listarPokemons, name="listar_pokemons"),
    path("pokemon/<int:idpokemon>/", umPokemon , name="um_pokemon")
]