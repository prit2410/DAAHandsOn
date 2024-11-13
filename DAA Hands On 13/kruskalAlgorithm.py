class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    edges = sorted(edges, key=lambda e: e.weight)
    uf = UnionFind(n)
    mst = []

    for edge in edges:
        if uf.find(edge.u) != uf.find(edge.v):
            uf.union(edge.u, edge.v)
            mst.append(edge)

    return mst

# Example usage of Kruskal's Algorithm
edges = [Edge(0, 1, 4), Edge(0, 2, 4), Edge(1, 2, 2), Edge(1, 3, 6), Edge(2, 3, 8)]
mst = kruskal(4, edges)
print("Kruskal's MST:")
for edge in mst:
    print(f"Edge {edge.u}-{edge.v} with weight {edge.weight}")
