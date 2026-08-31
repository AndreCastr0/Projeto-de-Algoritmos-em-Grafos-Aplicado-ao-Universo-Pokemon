import random
from pokemon import Pokemon



class Batalha:
    def __init__(self, treinador_desafiante, treinador_desafiado):
        self.treinador_desafiante = treinador_desafiante
        self.treinador_desafiado = treinador_desafiado

        self.time_desafiante = []
        self.time_desafiado = []

        self.pokemon_atual_desafiante = None
        self.pokemon_atual_desafiado = None

        self.tempo = 1

        self.vitorias = []
        self.derrotas = []

    def iniciar(self):
        #Seleciona os 3 Pokémon de cada treinador para o combate
        self.time_desafiante = escolher_pokemons_para_batalha(
            self.treinador_desafiante
        )

        if self.time_desafiante is None:
            print("O desafiante não possui 3 Pokémon conscientes.")

            return None

        self.time_desafiado = escolher_pokemons_para_batalha(
            self.treinador_desafiado
        )

        if self.time_desafiado is None:
            print("O desafiado não possui 3 Pokémon conscientes.")

            return None

        # Define os primeiros Pokémon a entrarem na arena

        self.pokemon_atual_desafiante = (
            self.time_desafiante[0]
        )

        self.pokemon_atual_desafiado = (
            self.time_desafiado[0]
        )

        print("\n BATALHA INICIADA ")

        return self.executar()



    def executar(self):
        # Controle de turnos do combate alternando os papéis de atacante e defensor
        atacante_eh_desafiado = True

        while True:

            if atacante_eh_desafiado:
                atacante = self.pokemon_atual_desafiado
                defensor = self.pokemon_atual_desafiante

                treinador_atacante = self.treinador_desafiado
                treinador_defensor = self.treinador_desafiante

            else:
                atacante = self.pokemon_atual_desafiante
                defensor = self.pokemon_atual_desafiado

                treinador_atacante = self.treinador_desafiante
                treinador_defensor = self.treinador_desafiado

            # Verifica opção de desistência antes de executar o turno

            if atacante_eh_desafiado:
                if verificar_desistencia(
                    self.treinador_desafiado
                ):
                    return self.finalizar(
                        vencedor=self.treinador_desafiante,
                        perdedor=self.treinador_desafiado
                    )


            print(
                f"\n{atacante.nome} "
                f"(HP: {atacante.hp}, XP: {atacante.xp}) "
                f"ataca "
                f"{defensor.nome} "
                f"(HP: {defensor.hp}, XP: {defensor.xp})"
            )

            escolher_ataque(atacante)

            dano, resultado = executar_ataque(
                atacante,
                defensor
            )

            if resultado == "esquiva":
                print(
                    f"{defensor.nome} conseguiu esquivar!"
                )

            elif resultado == "dobrado":
                print(
                    f"Golpe com dano dobrado!"
                )
                print(
                    f"{defensor.nome} recebeu "
                    f"{dano} de dano."
                )

            else:
                print(
                    f"{defensor.nome} recebeu "
                    f"{dano} de dano."
                )

            print(
                f"HP restante de {defensor.nome}: "
                f"{defensor.hp}"
            )

            # Verifica se o defensor ficou inconsciente
            
            if defensor.estado == Pokemon.INCONSCIENTE:

                print(
                    f"{defensor.nome} ficou inconsciente!"
                )

                # Registra o resultado do confronto.
                self.vitorias.append(atacante)
                self.derrotas.append(defensor)

                # Concede bônus se o atacante tinha XP maior ou igual ao defensor
                if atacante.xp >= defensor.xp:
                    atacante.adicionar_pontos_batalha()

                proximo = escolher_proximo_pokemon(
                    treinador_defensor,
                    (
                        self.time_desafiante
                        if not atacante_eh_desafiado
                        else self.time_desafiado
                    ),
                    defensor
                )

                if proximo is None:

                    # Não existem mais Pokémon conscientes.
                    return self.finalizar(
                        vencedor=treinador_atacante,
                        perdedor=treinador_defensor
                    )

                # Atualiza o Pokémon em campo do treinador que perdeu a rodada

                if atacante_eh_desafiado:
                    self.pokemon_atual_desafiante = proximo
                else:
                    self.pokemon_atual_desafiado = proximo

            # Alterna a vez de atacar
            
            atacante_eh_desafiado = not atacante_eh_desafiado


    def finalizar(self, vencedor, perdedor):
        print("\n FIM DA BATALHA")

        print(
            f"Vencedor: {vencedor.nome}"
        )

        print(
            f"Perdedor: {perdedor.nome}"
        )

        # Atribuição de experiência aos pokemons 

        for pokemon in self.vitorias:
            pokemon.adicionar_xp(10)

        for pokemon in self.derrotas:
            pokemon.adicionar_xp(3)

        # Atribuição de XP ao treinador

        if vencedor.xp >= perdedor.xp:
            vencedor.xp += 3
        else:
            vencedor.xp += 1

        # Retorno para o controle da jornada
      
        return {
            "vencedor": vencedor,
            "perdedor": perdedor,
            "tempo": self.tempo
        }


def verificar_desistencia(treinador):
    while True:
        resposta = input(
            f"\n{treinador.nome}, deseja desistir? (s/n): "
        ).lower()

        if resposta == "s":
            return True

        if resposta == "n":
            return False

        print("Digite 's' ou 'n'.")



def escolher_ataque(pokemon):
    #Exibe a lista de movimentos do Pokémon e solicita a seleção
    print(
        f"\nEscolha o ataque de {pokemon.nome}:"
    )

    for i, ataque in enumerate(pokemon.ataques):
        print(
            f"{i + 1} - {ataque[0]}"
        )

    while True:
        try:
            escolha = int(input("\nAtaque: "))

            if 1 <= escolha <= len(pokemon.ataques):
                return pokemon.ataques[escolha - 1]

            print("Escolha inválida.")

        except ValueError:
            print("Digite um número válido.")
            



def calcular_probabilidade(xp1, xp2):
    # Retorna uma probabilidade proporcional à diferença absoluta de XP entre os Pokémon
    diferenca = abs(xp1 - xp2)

    return min(diferenca / 100, 1.0)



def calcular_dano(atacante, defensor, dobro=False):
    # Calcula o dano causado com base no ataque (AP)
    dano = atacante.ap - defensor.dp

    if dano <= 0:
        return 0

    if dobro:
        dano *= 2

    return dano



def tentar_dano_dobrado(atacante, defensor):
    # Realiza o sorteio para aplicar dano dobrado baseado na probabilidade para fazer um ataque critico
    probabilidade = calcular_probabilidade(
        atacante.xp,
        defensor.xp
    )

    return random.random() < probabilidade




def tentar_esquiva(defensor, atacante):
    probabilidade = calcular_probabilidade(
        defensor.xp,
        atacante.xp
    )

    return random.random() < probabilidade



def executar_ataque(atacante, defensor):
    # Executa o fluxo completo do golpe
    if tentar_esquiva(defensor, atacante):
        return 0, "esquiva"

    dano_dobrado = tentar_dano_dobrado(atacante, defensor)

    dano = calcular_dano(
        atacante,
        defensor,
        dano_dobrado
    )

    defensor.hp = max(0, defensor.hp - dano)
    defensor.estado = defensor._definir_estado()

    if dano_dobrado:
        return dano, "dobrado"

    return dano, "normal"



def escolher_pokemons_para_batalha(treinador):
    # Permite selecionar interativamente 3 Pokémon conscientes
    disponiveis = [
        pokemon
        for pokemon in treinador.pokemons_ativos
        if pokemon.estado == Pokemon.CONSCIENTE
    ]

    if len(disponiveis) < 3:
        return None


    print("\nEscolha 3 Pokémon para a batalha:")

    for i, pokemon in enumerate(disponiveis):
        print(
            f"{i + 1} - {pokemon.nome} "
            f"(HP: {pokemon.hp}, "
            f"XP: {pokemon.xp})"
        )

    escolhidos = []

    while len(escolhidos) < 3:
        try:
            escolha = int(input("\nEscolha um Pokémon: "))

            if escolha < 1 or escolha > len(disponiveis):
                print("Escolha inválida.")
                continue

            pokemon = disponiveis[escolha - 1]

            if pokemon in escolhidos:
                print("Esse Pokémon já foi escolhido.")
                continue

            escolhidos.append(pokemon)

        except ValueError:
            print("Digite um número válido.")

    return escolhidos



def escolher_proximo_pokemon(treinador, time, pokemon_atual):
    # Permite selecionar o proximo pokemon
    disponiveis = [
        pokemon
        for pokemon in treinador.pokemons_ativos
        if pokemon.estado == Pokemon.CONSCIENTE
        and pokemon not in time
    ]

    if not disponiveis:
        return None

    print(
        f"\n{pokemon_atual.nome} ficou inconsciente."
    )

    print(
        f"{treinador.nome}, escolha o próximo Pokémon:"
    )

    for i, pokemon in enumerate(disponiveis):
        print(
            f"{i + 1} - {pokemon.nome} "
            f"(HP: {pokemon.hp}, XP: {pokemon.xp})"
        )

    while True:
        try:
            escolha = int(input("\nEscolha: "))

            if 1 <= escolha <= len(disponiveis):
                return disponiveis[escolha - 1]

            print("Escolha inválida.")

        except ValueError:
            print("Digite um número válido.")