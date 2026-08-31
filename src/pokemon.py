import csv
import ast
import random
from algorithms import dijkstra, reconstruir_caminho

class Pokemon:
    # Constantes para representação dos estados de saúde do Pokémon
    CONSCIENTE = "consciente"
    MACHUCADO = "machucado"
    INCONSCIENTE = "inconsciente"

    def __init__(
        self,
        id,
        posicao,
        nome,
        tipo1,
        tipo2,
        possibilidade_evolucao,
        fase_evolutiva,
        xp,
        hp,
        ap,
        dp,
        ataques
    ):
        self.id = id
        self.posicao = posicao

        # Informações da espécie
        self.nome = nome
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.possibilidade_evolucao = possibilidade_evolucao
        self.fase_evolutiva = fase_evolutiva
        self.ataques = ataques

        # Características da instância
        self.xp = xp
        self.hp = hp

        # Atributos base iniciais
        self.ap_inicial = ap
        self.dp_inicial = dp

        # Bônus acumulados em vitórias de duelos
        self.pontos_batalha_ap = 0
        self.pontos_batalha_dp = 0

        # Atributos atuais recalculados
        self.ap = ap
        self.dp = dp

        self.estado = self._definir_estado()

    def _definir_estado(self): #Avalia os pontos de HP oara definir a saude
        if self.hp == 0:
            return self.INCONSCIENTE
        elif 0 < self.hp < 5:
            return self.MACHUCADO
        else:
            return self.CONSCIENTE


    def adicionar_xp(self, quantidade): # Adiciona experiência e atualiza o ataque e a defesa
        self.xp += quantidade
        self.atualizar_ap_dp()

    def adicionar_pontos_batalha(self): # Concede bônus fixo de AP/DP por vitória em duelo com rival de XP igual ou maior
        self.pontos_batalha_ap += 1
        self.pontos_batalha_dp += 1
        self.atualizar_ap_dp()


    def atualizar_ap_dp(self): #10%
        # Recalcula AP e DP: valor inicial + 10% do XP total + bônus de duelos
        self.ap = (self.ap_inicial + (0.10 * self.xp) + self.pontos_batalha_ap)

        self.dp = (self.dp_inicial + (0.10 * self.xp) + self.pontos_batalha_dp)       


def ler_pokedex(path): # Carrega a Pokédex a partir de um arquivo CSV
    pokedex = []

    with open(path, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            pokemon = {
                "pokedex_no": int(linha["pokedex_no"]),
                "name": linha["name"],
                "type1": linha["type1"],
                "type2": linha["type2"] if linha["type2"] else None,
                "moves": ast.literal_eval(linha["moves"]),
                "pode_evoluir": int(linha["pode_evoluir"]),
                "fase_evolutiva": int(linha["fase_evolutiva"])
            }

            pokedex.append(pokemon)

    return pokedex


def criar_pokemon(numero_vertices, pokedex): # Sorteia uma espécie da Pokédex e atribui atributos aleatórios
    especie = random.choice(pokedex)

    pokemon = Pokemon(
        id=especie["pokedex_no"],
        posicao=random.randint(1, numero_vertices),
        nome=especie["name"],
        tipo1=especie["type1"],
        tipo2=especie["type2"],
        possibilidade_evolucao=especie["pode_evoluir"],
        fase_evolutiva=especie["fase_evolutiva"],
        xp=0,
        hp=random.randint(1, 100),
        ap=random.randint(1, 100),
        dp=random.randint(1, 100),
        ataques=especie["moves"]
    )

    return pokemon


def criar_pokemons(quantidade, numero_vertices, pokedex):
    # Instancia uma lista contendo a quantidade desejada de Pokémon aleatórios
    pokemons = []

    for i in range(quantidade):
        pokemon = criar_pokemon(
            numero_vertices=numero_vertices,
            pokedex=pokedex
        )

        pokemons.append(pokemon)

    return pokemons


def criar_pokemon_da_especie(pokedex_no, posicao, pokedex):
    # Instancia um Pokémon de uma espécie específica buscando por seu índice na Pokédex
    especie = pokedex[pokedex_no]
    
    pokemon = Pokemon(
        id=pokedex_no,
        posicao=posicao,
        nome=especie["name"],
        tipo1=especie["type1"],
        tipo2=especie["type2"],
        possibilidade_evolucao=especie["pode_evoluir"],
        fase_evolutiva=especie["fase_evolutiva"],
        xp=0,
        hp=random.randint(1, 100),
        ap=random.randint(1, 100),
        dp=random.randint(1, 100),
        ataques=especie["moves"]
    )

    return pokemon





