from utils import read_input
from graph import Graph
from treinador import Treinador
from pokemon import Pokemon, ler_pokedex, criar_pokemons, criar_pokemon_da_especie


def main():
    # 1. Carregando os dados e construindo o grafo
    dados = read_input("data/data.txt")
    pokedex = ler_pokedex("data/kanto.csv")
    

if __name__ == "__main__":
    main()