class Pokemon:
    CONSCIENTE = "consciente"  #hp > 5
    MACHUCADO = "machucado"    #hp <= 5
    INCONSCIENTE = "inconsciente" #hp == 0

    def __init__(
        self,
        id,
        posicao,
        tipo,
        pode_evoluir,
        fase_evolutiva,
        xp,
        hp,
        ap,
        dp,
        ataques
    ):
        self.id = id
        self.posicao = posicao
        self.tipo = tipo
        self.pode_evoluir = pode_evoluir
        self.fase_evolutiva = fase_evolutiva
        self.xp = xp
        self.hp = hp
        self.ap = ap
        self.dp = dp
        self.estado = self._definir_estado()
        self.ataques = ataques

    def _definir_estado(self):
        if self.hp == 0:
            return self.INCONSCIENTE
        elif 0 < self.hp <= 5:
            return self.MACHUCADO
        else:
            return self.CONSCIENTE


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
        insignias=None
    ):
        self.posicao = posicao
        self.xp = xp
        self.pokemons_ativos = pokemons_ativos if pokemons_ativos is not None else []
        self.pokemons_excedentes = (
            pokemons_excedentes if pokemons_excedentes is not None else []
        )
        self.pokebolas = pokebolas
        self.incubadoras = incubadoras
        self.insignias = insignias if insignias is not None else set()