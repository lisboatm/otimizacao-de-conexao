class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Compressão de caminho
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # União por ranking
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

# Leitura da entrada
R, C = map(int, input().split())
edges = []

for _ in range(C):
    V, W, P = map(int, input().split())
    edges.append((P, V - 1, W - 1))  # Ajuste para índices baseados em zero

# Ordena as arestas pelo peso (custo)
edges.sort()

# Inicializa a estrutura de Union-Find
uf = UnionFind(R)

# Algoritmo de Kruskal para encontrar a MST
mst_cost = 0
edges_used = 0

for cost, u, v in edges:
    if uf.union(u, v):
        mst_cost += cost
        edges_used += 1
        # Termina quando temos R-1 arestas na MST
        if edges_used == R - 1:
            break

# Saída do custo total da MST
print(mst_cost)
