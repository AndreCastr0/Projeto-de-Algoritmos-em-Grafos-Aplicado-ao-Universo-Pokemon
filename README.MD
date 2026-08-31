# Simulador de Jornada Pokemon em Grafos

Projeto desenvolvido para a disciplina de **Algoritmos em Grafos** e não está completo.

## 1. Proposta do projeto

O projeto consiste na implementação de uma simulação de uma jornada Pokémon em uma região representada por um grafo ponderado.

O jogador assume o papel de um treinador Pokémon que deve percorrer a região, capturar Pokémon selvagens, batalhar contra outros treinadores e Líderes de Ginásio, conquistar insígnias e, ao final da jornada, estar apto a se inscrever na Liga Pokémon.

O mapa da região é representado por um grafo, no qual:

- os vértices representam locais da região;
- as arestas representam caminhos entre locais;
- os pesos das arestas representam o tempo necessário para percorrer cada caminho.

O treinador pode se deslocar livremente pelo mapa, podendo utilizar uma mesma aresta ou vértice diversas vezes.

O objetivo final é obter as insígnias necessárias e chegar ao local de inscrição da Liga dentro do prazo estabelecido.

---

## 2. 📁 Estrutura do Projeto

```text
.
├── main.py          # Ponto de entrada. Controlaria o fluxo principal da jornada
├── algorithms.py    # Algoritmo de Dijkstra (Usado pelos treinadores e pokemons)
├── graph.py         # Estrutura de dados do grafo (lista de adjacência)
├── treinador.py     # Implementa a classe Treinador, seus atributos e métodos
├── pokemon.py       # A classe representa os Pokémon existentes e suas informações
├── Batalha.py       # Contém a estrutura responsável pelas batalhas. Atualmente, o arquivo possui a estrutura inicial para batalhas entre treinadores, incluindo seleção dos Pokémon, turnos, ataques, dano, esquiva, dano dobrado, substituição de Pokémon e distribuição de XP
├── utils.py         # Leitura e manipulação do arquivo de entrada
└── data/
    ├── data.txt     # Arquivo de entrada com a configuração do cenário
    └── kanto.txt    # dataset customizado completo da primeira geração de pokemons e dados necessários
```

---

## 3. ⚙️ Como Executar (Veja os códigos, o projeto está incompleto)

**Pré-requisito:** Python 3.x.

1. Clone o repositório ou baixe os arquivos.

2. Execute:

```bash
python main.py
```

---

## 4. 📄 Formato do Arquivo de Entrada

O arquivo `data.txt` descreve a região, posições, quantidades de pokemons, itens e diversos outros elementos para construir o estado inicial.

| Chave | Significado | Exemplo | Descrição |
|---|---|---|---|
| `n` | Número de vértices | `n 7` | O grafo possui 7 vértices |
| `m` | Número de arestas | `m 8` | O grafo possui 8 arestas |
| `w` | Aresta bidirecionada positiva | `w 1 2 1` | Aresta de `1` → `2` com peso `1` |
| `p` | Quantidade de pokemons | `p 7` | Existe 7 pokemons no mapa |
| `t` | Quantidade de treinadores | `t 3` | Existem 3 treinadores nao lideres |
| `o` | Quantidade de ovos | `o 5` | Existem 5 ovos |
| `e` | Quantidade de ervas | `t 3` | Existem 3 ovos |
| `g` | Quantidade de ginasios | `o` | Existem 8 lideres de ginasios |
| `h` | Quantidade de PMC | `o 2` | Existem 2 centros pokemons |

O professor carvalho sempre é posicionado na origem.

### Exemplo de entrada (`data.txt`)

```text
n 10

m 11

w 1 2 1
w 2 3 1
w 3 7 1
w 1 4 5
w 4 5 5
w 5 6 5
w 6 7 1
w 5 2 1
w 8 9 2
w 9 10 1
w 9 7 3

p 5
t 3
o 2
e 4
g 8
h 6
c 1
```

---

## 5. Geração aleatória dos elementos

O arquivo de entrada define principalmente quantidades.

Por exemplo:

```text
p 5
t 3
o 2
e 4
g 8
h 6
```

Isso não determina que um Pokémon esteja no vértice 5 ou que um treinador esteja no vértice 3.

Ele apenas determina que devem existir:

- 5 Pokémon;
- 3 treinadores;
- 2 ovos;
- 4 ervas;
- 8 ginásios;
- 6 Centros Pokémon.

---

## 6. Arquivo `kanto.csv`

Além do arquivo de descrição do grafo, o projeto utiliza o arquivo `kanto.csv`, contendo os 151 Pokémon da região de Kanto.

A estrutura do arquivo possui informações como:

```text
pokedex_no
name
type1
type2
moves
hp
attack
defense
special-attack
pode_evoluir
fase_evolutiva
```

### Exemplo

```text
1,bulbasaur,grass,poison,...
2,ivysaur,grass,poison,...
```

Os valores de HP, ataque e defesa presentes no arquivo não são utilizados.

Quando um Pokémon é criado, seus valores de HP, AP e DP são gerados aleatoriamente conforme as regras adotadas na implementação.

A espécie de um Pokémon selvagem é escolhida aleatoriamente utilizando um número entre 1 e 151, que corresponde ao pokedex_no.

---

# 7. Mecânicas do projeto

## 7.1 Inicialização da região

O programa começa lendo o arquivo de entrada por meio da função `read_input()`.

A função interpreta cada linha de acordo com seu identificador (`n`, `m`, `w`, `p`, `t`, `o`, `e`, `g`, `h`) e retorna as informações separadas em variáveis.

A partir das arestas lidas, o objeto `Graph` é construído. Como as conexões da região são não direcionadas, cada aresta é adicionada nos dois sentidos na lista de adjacência.

As quantidades de Pokémon, treinadores, ovos, ervas, ginásios e Centros Pokémon são utilizadas posteriormente para gerar esses elementos na região. Suas posições não são definidas diretamente pelo arquivo, sendo determinadas pelo programa.

O laboratório do Professor Carvalho possui uma única ocorrência e não é informado no arquivo de entrada. Sua posição é definida pelo programa como o ponto inicial da jornada.

---

## 7.2 Pokémon

Os dados das espécies são carregados a partir do arquivo `kanto.csv`, que contém os 151 Pokémon da região de Kanto.

Quando um Pokémon é criado, o programa escolhe aleatoriamente um `pokedex_no` entre 1 e 151 e utiliza esse identificador para buscar os dados da espécie na Pokédex.

Os dados da espécie, como nome, tipos, ataques, possibilidade de evolução e fase evolutiva, são copiados para o novo objeto `Pokemon`.

Os valores de HP, AP e DP são gerados aleatoriamente no momento da criação, independentemente dos valores presentes no CSV.

Cada Pokémon pode possuir um ou dois tipos, armazenados nos atributos `tipo1` e `tipo2`.

---

## 7.3 Treinadores e equipe

A classe `Treinador` representa tanto o personagem principal quanto os demais treinadores.

A mesma classe também pode representar treinadores inimigos e Líderes de Ginásio por meio de atributos que identificam essas características.

Cada treinador possui uma lista de Pokémon ativos e uma lista de Pokémon excedentes.

A equipe ativa é limitada a seis Pokémon. Quando o treinador captura ou recebe um novo Pokémon e já possui seis ativos, é necessário escolher qual Pokémon continuará na equipe e qual será enviado para a lista de excedentes.

---

## 7.4 Pokémon iniciais

Na criação do personagem, os três Pokémon iniciais são obtidos diretamente pelos números da Pokédex:

```text
1 → Bulbasaur (indice 0)
4 → Charmander (indice 3)
7 → Squirtle (indice 6)
```

---

## 7.5 Movimentação

A movimentação do treinador é realizada sobre o objeto `Graph`.

Cada aresta possui um peso que representa o tempo necessário para percorrer aquele caminho.

Para encontrar o caminho de menor custo entre a posição atual e um destino, foi implementado o algoritmo de Dijkstra.

A movimentação atualiza a posição do treinador e, consequentemente, dos Pokémon que estão acompanhando o treinador.

O tempo gasto no deslocamento é obtido pela soma dos pesos das arestas percorridas e armazenado no controle de tempo da jornada.

Além disso, a distância percorrida pode ser utilizada para determinar o ganho de XP dos Pokémon.

---

## 7.6 Controle de tempo

O projeto mantém o tempo acumulado da jornada em uma variável de controle.

Quando o treinador percorre uma aresta, o peso dessa aresta é acrescentado ao tempo total.

---

## 7.7 Captura e gerenciamento de Pokémon

Quando o treinador encontra um Pokémon selvagem, pode ocorrer uma batalha (Não totalmente implementada).

Após uma captura bem-sucedida, uma Pokébola é consumida e o Pokémon é adicionado à equipe por meio da lógica já existente de gerenciamento de Pokémon.

Caso a equipe possua seis Pokémon, o treinador precisa escolher qual Pokémon permanecerá entre os ativos e qual será colocado como excedente.

---

## 7.8 Batalhas

As batalhas foram separadas em um módulo próprio, `batalha.py`.

Uma batalha entre treinadores recebe dois objetos `Treinador`:

Inicialmente, cada treinador escolhe três Pokémon conscientes para participar.

O treinador desafiado começa a batalha.

A cada turno, o Pokémon atacante escolhe um de seus ataques e o dano é calculado utilizando os atributos AP do atacante e DP do defensor.

Durante o ataque também são verificadas as possibilidades de esquiva e de dano dobrado.

Quando um Pokémon chega a zero de HP, seu estado passa para `INCONSCIENTE` e ele não pode continuar lutando. O treinador então escolhe outro Pokémon consciente para substituí-lo.

A batalha continua até que um dos treinadores não possua mais Pokémon disponíveis para lutar ou ocorra uma desistência.

Os resultados dos confrontos individuais são armazenados para que, ao final da batalha, seja possível distribuir o XP correspondente aos Pokémon.

---

## 7.9 XP e atributos dos Pokémon

O XP dos Pokémon é controlado diretamente pela classe `Pokemon`.

Ao receber XP, o Pokémon atualiza seus atributos relacionados ao crescimento, mantendo a evolução de AP e DP vinculada ao XP acumulado.

Nas batalhas, os Pokémon vencedores e derrotados recebem quantidades diferentes de XP de acordo com o resultado do confronto.

O deslocamento pelo mapa também contribui para o ganho de XP, relacionando o crescimento dos Pokémon à distância percorrida pelo treinador.

---

# 8. 🔬 Algoritmos Utilizados

## Algoritmo de percurso — Dijkstra

O algoritmo escolhido para determinar os caminhos de movimentação do treinador é o algoritmo de Dijkstra.

A escolha se deve principalmente às características do grafo utilizado no projeto.

As arestas possuem pesos que representam o tempo necessário para percorrer cada caminho e esses pesos são não negativos.

O objetivo é encontrar caminhos de menor custo entre vértices, o que corresponde diretamente a encontrar caminhos que minimizem o tempo de deslocamento.

A implementação utiliza uma estrutura de prioridade para selecionar da forma `mais eficiente` o próximo vértice de menor distância.