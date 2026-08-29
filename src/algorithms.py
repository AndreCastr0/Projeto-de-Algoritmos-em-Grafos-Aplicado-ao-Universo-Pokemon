import heapq


def dijkstra(graph, origem): #grafo em forma de lista de adj e a origem
    distancias = [float('inf')] * (graph.n + 1) #distancias infinitas 
    predecessores = [None] * (graph.n + 1) #lista vazia com o tamanho real do grafo para armazenas os predecessores

    distancias[origem] = 0 #distancia do ponto de partida

    heap = [(0, origem)] #coloca a origem na fila de prioridade

    while heap:
        distancia_atual, u = heapq.heappop(heap) #enquanto a fila nao estiver vazia, eu removo o vértice mais próximo

        if distancia_atual > distancias[u]: 
            continue

        for v, peso in graph.get_neighbors(u): #atualizando com base na distancia atual e o custo do vizinho
            nova_distancia = distancia_atual + peso

            if nova_distancia < distancias[v]: #"Se eu for por aqui, o caminho total fica mais curto do que o que eu já conhecia?"
                distancias[v] = nova_distancia
                predecessores[v] = u

                heapq.heappush(heap, (nova_distancia, v))

    return distancias, predecessores

    #Exemplo:
    #predecessores[7] = 5
    #predecessores[5] = 2
    #predecessores[2] = 1


def reconstruir_caminho(predecessores, origem, destino): #"Eu cheguei aqui através de qual vértice?" Olha o vértice anterior no caminho
    caminho = []

    atual = destino

    while atual is not None:
        caminho.append(atual)

        if atual == origem:
            break

        atual = predecessores[atual]

    if caminho[-1] != origem:
        return []

    caminho.reverse()

    return caminho #retorna o menor caminho entre a origem e o destino 