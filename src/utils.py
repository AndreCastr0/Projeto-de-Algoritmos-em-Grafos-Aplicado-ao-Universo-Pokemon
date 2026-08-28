def read_input(path):
    n = 0 #numero de vértices
    m = 0 #numero de arestas
    w_edges = [] #lista de conexões

    #quantidades areatórias dentro de uma faixa e posições aleatórias 
    q_pokemons = 0
    q_trainers = 0
    q_eggs = 0
    q_herbs = 0
    q_gyms = 0 

    pokemon_center = None #lista de localizações dos centros pokemon
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
            pokemon_center = int(tokens[1]) #vertices que representam as localizações dos centros pokemon

        elif key == 'c':
            professor_carvalho = int(tokens[1]) #vertice que representa a localização do Lab professor carvalho
            

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