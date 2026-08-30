from algorithms import dijkstra, reconstruir_caminho

class Treinador:
    MAX_POKEMONS_ATIVOS = 6
    MAX_POKEMONS_TOTAL = 7

    def __init__(
        self,
        posicao,
        xp,
        pokemons_ativos=None,
        pokemons_excedentes=None,
        pokebolas=7,
        incubadoras=1,
        insignias=None,
        inimigo=False,
        lider_ginasio=False
    ):
        self.posicao = posicao
        self.xp = xp

        self.pokemons_ativos = (
            pokemons_ativos if pokemons_ativos is not None else []
        )

        self.pokemons_excedentes = (
            pokemons_excedentes if pokemons_excedentes is not None else []
        )

        self.pokebolas = pokebolas
        self.incubadoras = incubadoras

        self.insignias = (
            insignias if insignias is not None else set()
        )

        self.inimigo = inimigo
        self.lider_ginasio = lider_ginasio

        self.distancia_percorrida = 0


    def mover(self, graph, destino):

        distancias, predecessores = dijkstra(graph, self.posicao)

        caminho = reconstruir_caminho(
            predecessores,
            self.posicao,
            destino
        )

        if not caminho:
            return [], 0

        tempo_gasto = 0

        for i in range(len(caminho) - 1):
            atual = caminho[i]
            proximo = caminho[i + 1]

            peso = graph.get_edge_weight(atual, proximo)

            self.posicao = proximo
            tempo_gasto += peso

        return caminho, tempo_gasto
    


    def adicionar_pokemon(self, pokemon):
        if len(self.pokemons_ativos) < self.MAX_POKEMONS_ATIVOS:
            self.pokemons_ativos.append(pokemon)
            pokemon.posicao = self.posicao
            return "ativo"

        if len(self.pokemons_excedentes) < (
            self.MAX_POKEMONS_TOTAL - self.MAX_POKEMONS_ATIVOS
        ):
            self.pokemons_excedentes.append(pokemon)
            return "excedente"

        return None


      