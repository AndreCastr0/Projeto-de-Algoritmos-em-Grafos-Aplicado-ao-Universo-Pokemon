
class Graph:
    def __init__(self, n_vertices):
        self.n = n_vertices

        # cria uma lista vazia para cada vértice
        self.adj_list = []

        # Fazemos (n + 1) para o vértice 1 ficar exatamente na posição 1 da lista.
        for i in range(n_vertices + 1):
            self.adj_list.append([])

    def add_edge(self, u, v, weight):
        # Vai direto na posição 'u' da lista e adiciona a tupla 
        #EX: adj_list[1] = [(2, 5)] significa: "há uma aresta de 1 para 2 e tem peso 5"

        self.adj_list[u].append((v, weight)) #conexões em ambas as direções
        self.adj_list[v].append((u, weight))

    def get_neighbors(self, u):
        # Retorna a lista de vizinhos do elemento que está na posição 'u'
        return self.adj_list[u]

    def get_edge_weight(self, u, v): #busca o peso da aresta que liga (u --> v). Usado para atualizar o tempo
        for neighbor, weight in self.adj_list[u]:
            if neighbor == v:
                return weight

        return None

    def get_all_edges(self):
        # Pega todas as arestas
        edges = []

        #Monta e retorna uma lista composta por tuplas no formato (u, v, weight) com todas as ligações do grafo.       
        for u in range(1, self.n + 1):
            for v, weight in self.adj_list[u]:
                edges.append((u, v, weight))

        return edges