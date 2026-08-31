from graph import Graph


def read_input(path): #extrai os dados da entrada
    n = 0 #numero de vértices
    m = 0 #numero de arestas
    w_edges = [] #lista de conexões

    #quantidades areatórias dentro de uma faixa e posições aleatórias 
    q_pokemons = 0
    q_trainers = 0
    q_eggs = 0
    q_herbs = 0
    q_gyms = 0 

    pokemon_centers = None #lista de localizações dos centros pokemon
    professor_carvalho = None
    

    with open(path, 'r') as f: #leitura de arquivo
        lines = f.readlines()

    for line in lines: #line assume o papel de uma linha por vez
        tokens = line.split()  #primeira palavra,

        if not tokens:
            continue #pula para a próxima linha se a linha atual estiver vazia

        key = tokens[0] # primeira letra

        #Informações extraídas do arquivo:

        if key == 'n': 
            n = int(tokens[1])

        elif key == 'm':
            m = int(tokens[1])

        elif key == 'w':
            u, v, weight = map(int, tokens[1:])
            w_edges.append((u, v, weight))

        elif key == 'p':
            q_pokemons = int(tokens[1])

        elif key == 't':
            q_trainers = int(tokens[1])

        elif key == 'o':
            q_eggs = int(tokens[1])

        elif key == 'e':
            q_herbs = int(tokens[1])

        elif key == 'g':
            q_gyms = int(tokens[1])

        elif key == 'h':
            pokemon_centers = int(tokens[1]) #vertices que representam as localizações dos centros pokemon

    

    return (
        n,
        m,
        w_edges,
        q_pokemons,
        q_trainers,
        q_eggs,
        q_herbs,
        q_gyms,
        pokemon_centers,
        professor_carvalho,
    )




def exibir_listas_grafo(graph, n):
    print("Lista de adjacência:")

    for u in range(1, n + 1):
        vizinhos = graph.get_neighbors(u)

        linha = f"[v{u}]"

        for v, weight in vizinhos:
            linha += f" ---{weight}---> [v{v}]"

        print(linha)
        print("\n")



def exibir_dados_arquivo(dados):
    print("----Exibindo data.txt--- \n")

    n = dados[0]
    m = dados[1]
    w_edges = dados[2]

    q_pokemons = dados[3]
    q_trainers = dados[4]
    q_eggs = dados[5]
    q_herbs = dados[6]
    q_gyms = dados[7]
    pokemon_center = dados[8]
    professor_carvalho = dados[9]

    print("Número de vértices:", n)
    print("Número de arestas:", m)

    print("\nArestas:")
    for u, v, weight in w_edges:
        print(f"{u} -- {v} (peso: {weight})")

    print("\nQuantidade de Pokémon:", q_pokemons)
    print("Quantidade de treinadores:", q_trainers)
    print("Quantidade de ovos:", q_eggs)
    print("Quantidade de ervas:", q_herbs)
    print("Quantidade de ginásios:", q_gyms)

    print("\nQuantidade de centros pokemon:", pokemon_center)
    print("Localização do laboratório do professor:", professor_carvalho)

