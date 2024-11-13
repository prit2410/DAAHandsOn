class Edge:
    def __init__(self, weight, u, v):
        self.weight = weight
        self.u = u
        self.v = v

class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

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

def kruskal(nodes, edges):
    edges = sorted(edges, key=lambda e: e.weight)
    uf = UnionFind(nodes)
    mst = []

    for edge in edges:
        if uf.find(edge.u) != uf.find(edge.v):
            uf.union(edge.u, edge.v)
            mst.append(edge)

    return mst

# Define nodes and edges for Kruskal's example
nodes_kruskal = {"a", "b", "c", "d", "e", "f", "g", "h", "i"}
edges_kruskal = [
    Edge(4, "a", "b"),
    Edge(8, "a", "h"),
    Edge(8, "b", "c"),
    Edge(11, "b", "h"),
    Edge(7, "c", "d"),
    Edge(4, "c", "f"),
    Edge(2, "c", "i"),
    Edge(6, "c", "g"),
    Edge(9, "d", "e"),
    Edge(14, "d", "f"),
    Edge(10, "e", "f"),
    Edge(2, "f", "g"),
    Edge(1, "g", "h"),
    Edge(7, "h", "i")
]

# Perform Kruskal's MST
mst = kruskal(nodes_kruskal, edges_kruskal)
print("Kruskal's MST:")
for edge in mst:
    print(f"Edge {edge.u}-{edge.v} with weight {edge.weight}")
