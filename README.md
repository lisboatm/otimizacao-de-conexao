# README - Desafio C: Otimização de Conexões em Redes com MST (Algoritmo de Kruskal)

## Descrição do Problema

Bruno é o responsável por configurar os roteadores de uma empresa. Os roteadores são conectados por cabos de rede, e a empresa deseja minimizar o custo total dessas conexões mantendo todos os roteadores conectados entre si. A ideia é que cada par de roteadores seja conectado por **apenas uma rota** e, ao mesmo tempo, que o custo total seja o menor possível.

Você foi solicitado a resolver este problema utilizando técnicas de **Teoria dos Grafos**, especificamente para encontrar a **Árvore Geradora Mínima (MST)** usando o **Algoritmo de Kruskal**.

## Entrada

A entrada é composta por:
1. Dois inteiros **R** (número de roteadores) e **C** (número de cabos de rede).
2. Seguem **C linhas**, cada uma contendo três inteiros:
   - **V** e **W** (roteadores conectados pelo cabo).
   - **P** (custo do cabo de conexão entre os roteadores V e W).

### Restrições
- **3 ≤ R ≤ 60** (número de roteadores)
- **R ≤ C ≤ 200** (número de cabos)
- **1 ≤ V, W ≤ R** (identificadores dos roteadores)
- **1 ≤ P ≤ 10,000** (custo de cada cabo)

## Saída

A saída deve ser um único inteiro que representa o **custo total mínimo** dos cabos utilizados após as modificações.

### Exemplo de Entrada
```
7 12
1 3 6
1 4 9
2 3 17
2 5 32
2 7 27
3 4 11
3 5 4
4 5 3
4 6 19
5 6 13
5 7 15
6 7 5
```

### Exemplo de Saída
```
48
```

### Explicação
- Utilizando o **Algoritmo de Kruskal**, determinamos a **Árvore Geradora Mínima (MST)** que conecta todos os roteadores com o menor custo possível.

## Implementação em Python

O código a seguir utiliza o **Algoritmo de Kruskal** com a estrutura de **Union-Find** para resolver o problema de forma eficiente.

### Código

```python
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
```

## Explicação do Código

1. **Union-Find**:
   - Usamos a estrutura de dados `Union-Find` para detectar ciclos e gerenciar a união de conjuntos de roteadores.
   - `find(u)`: Encontra o representante (raiz) do conjunto ao qual `u` pertence.
   - `union(u, v)`: Une os conjuntos de `u` e `v` se eles não estiverem já conectados.

2. **Leitura da Entrada**:
   - Lemos o número de roteadores `R` e cabos `C`.
   - Em seguida, lemos as conexões, onde cada conexão é descrita por dois roteadores `V`, `W` e o custo `P`.

3. **Algoritmo de Kruskal**:
   - Ordenamos as arestas (cabos) pelo custo.
   - Iteramos pelas arestas ordenadas, utilizando o `Union-Find` para garantir que não formamos ciclos.
   - Somamos o custo das arestas que fazem parte da MST.
   - O algoritmo para quando usamos `R-1` arestas.

## Complexidade

- **Tempo**: O algoritmo é eficiente, com complexidade **O(C log C)**, onde `C` é o número de cabos.
- **Espaço**: O uso de `Union-Find` garante uma utilização eficiente da memória.

## Como Executar o Código

Certifique-se de ter **Python 3** instalado no seu sistema. Para executar o programa:

1. Salve o código em um arquivo, por exemplo, `desafio_c.py`.
2. Abra o terminal e navegue até o diretório onde o arquivo foi salvo.
3. Execute o programa com:
   ```bash
   python otimizacao_de_conexao.py
   ```
4. Insira os dados manualmente ou redirecione a entrada a partir de um arquivo:
   ```bash
   python otimizacao_de_conexao.py < input.txt
   ```

## Conclusão

O **Desafio C** é uma aplicação prática de algoritmos de grafos e técnicas de otimização usando **Árvores Geradoras Mínimas**. Utilizar o **Algoritmo de Kruskal** juntamente com o **Union-Find** garante uma solução eficiente, mesmo para entradas grandes.
