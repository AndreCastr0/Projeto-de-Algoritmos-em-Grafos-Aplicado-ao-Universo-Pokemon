
class Graph:
    def __init__(self, n_vertices):
        self.n = n_vertices

        #cria uma listavazia para cada vértice
        self.adj_list = []

        # Fazemos (n + 1) para o vértice 1 ficar exatamente na posição 1 da lista.
        for i in range(n_vertices + 1):
            self.adj_list.append([])

    def add_edge(self, u, v, weight):
        # Vai direto na posição 'u' da lista e adiciona a tupla 
        #EX: adj_list[1] = [(2, 5)] "há uma aresta de 1 para 2 e tem peso 5"

        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))

    def get_neighbors(self, u):
        # Retorna a lista de vizinhos que está na posição 'u'
        return self.adj_list[u]

    def get_all_edges(self):
        # Pega todas as arestas
        edges = []

        for u in range(1, self.n + 1):
            for v, weight in self.adj_list[u]:
                edges.append((u, v, weight))

        return edges