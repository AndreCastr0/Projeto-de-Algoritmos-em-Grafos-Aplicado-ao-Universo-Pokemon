from algorithms import dijkstra, reconstruir_caminho

class Treinador:
    MAX_POKEMONS_ATIVOS = 6 #os pokemons que passarem dessa quantidade são os que o professor esta armazenando

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
            pokemons_ativos
            if pokemons_ativos is not None
            else []
        )

        self.pokemons_excedentes = ( #São os pokemons com o professor carvalho
            pokemons_excedentes
            if pokemons_excedentes is not None
            else []
        )

        self.pokebolas = pokebolas
        self.incubadoras = incubadoras

        self.insignias = (
            insignias if insignias is not None else set()
        )

        self.inimigo = inimigo
        self.lider_ginasio = lider_ginasio

        self.distancia_percorrida = 0
        self.ultimo_xp_distancia = 0


    def mover(self, graph, destino):

        distancias, predecessores = dijkstra(graph,self.posicao)

        caminho = reconstruir_caminho(predecessores,self.posicao,destino)

        if not caminho:
            return [], 0

        tempo_gasto = 0

        for i in range(len(caminho) - 1):
            atual = caminho[i]
            proximo = caminho[i + 1]

            peso = graph.get_edge_weight(atual,proximo)

            # O treinador se move.
            self.posicao = proximo

            # Os Pokémon ativos acompanham o treinador.
            for pokemon in self.pokemons_ativos:
                pokemon.posicao = proximo

            # Atualiza a distância total.
            self.distancia_percorrida += peso

            # O peso da aresta representa o tempo/distância
            # percorrido na jornada.
            tempo_gasto += peso

            # XP por distância.
            self._atualizar_xp_distancia()

        return caminho, tempo_gasto


    def capturar_pokemon(self, pokemon, pokemons_batalha=None):
        if pokemon.estado != pokemon.INCONSCIENTE:
            return False

        if self.pokebolas <= 0:
            return False

        self.pokebolas -= 1

        # XP pela captura.
        self.xp += 3

        if pokemons_batalha is not None:
            for pokemon_batalha in pokemons_batalha:
                pokemon_batalha.adicionar_xp(3)

        # Adiciona o Pokémon aos ativos ou solicita
        # uma escolha caso já existam 6.
        self.escolher_pokemon_ativo(pokemon)

        return True
    


    def _atualizar_xp_distancia(self):
        xp_atual = self.distancia_percorrida // 100

        xp_novo = xp_atual - self.ultimo_xp_distancia

        if xp_novo > 0:
            for pokemon in self.pokemons_ativos:
                pokemon.adicionar_xp(xp_novo)

            self.ultimo_xp_distancia = xp_atual
    


    def adicionar_pokemon(self, pokemon): #adicionar um pokemon que acabou de ser capturado
        if len(self.pokemons_ativos) < self.MAX_POKEMONS_ATIVOS:
            self.pokemons_ativos.append(pokemon)
            pokemon.posicao = self.posicao
            return "ativo"

        # Já possui 6 ativos. O pokémon é adicionado temporariamente aos excedentes.
        self.pokemons_excedentes.append(pokemon)

        return "excedente"


    def trocar_pokemon(self, pokemon_ativo, pokemon_excedente): #trocar entre pokemon ativo e excedente
        if pokemon_ativo not in self.pokemons_ativos:
            return False

        if pokemon_excedente not in self.pokemons_excedentes:
            return False

        self.pokemons_ativos.remove(pokemon_ativo)
        self.pokemons_excedentes.remove(pokemon_excedente)

        self.pokemons_excedentes.append(pokemon_ativo)

        self.pokemons_ativos.append(pokemon_excedente)

        pokemon_excedente.posicao = self.posicao

        return True



    def escolher_pokemon_ativo(self, pokemon):
        if len(self.pokemons_ativos) < self.MAX_POKEMONS_ATIVOS:
            self.pokemons_ativos.append(pokemon)
            pokemon.posicao = self.posicao
            return True

        print("\nVocê já possui 6 Pokémon ativos.")
        print("Escolha qual Pokémon deseja enviar ao Professor Carvalho.")

        for i, pokemon_ativo in enumerate(self.pokemons_ativos):
            print(
                f"{i + 1} - "
                f"{pokemon_ativo.nome} "
                f"(Pokedex #{pokemon_ativo.id})"
            )

        while True:
            try:
                escolha = int(input("\nEscolha: "))

                if 1 <= escolha <= len(self.pokemons_ativos):
                    break

                print("Escolha inválida.")

            except ValueError:
                print("Digite um número válido.")

        pokemon_enviado = self.pokemons_ativos.pop(escolha - 1)

        self.pokemons_excedentes.append(pokemon_enviado)

        self.pokemons_ativos.append(pokemon)

        pokemon.posicao = self.posicao

        return True
      