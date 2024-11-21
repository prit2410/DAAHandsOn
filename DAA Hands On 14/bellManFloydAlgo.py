class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, source):
        # Step 1: Initialize distances
        distances = {v: float('inf') for v in self.vertices}
        distances[source] = 0

        # Step 2: Relax edges repeatedly
        for _ in range(len(self.vertices) - 1):
            for u, v, weight in self.edges:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        # Step 3: Check for negative weight cycles
        for u, v, weight in self.edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")

        return distances


# Create graph and add edges
vertices = ['s', 't', 'x', 'y', 'z']
graph = Graph(vertices)

# Add edges (u, v, weight)
graph.add_edge('s', 't', 6)
graph.add_edge('s', 'y', 7)
graph.add_edge('t', 'x', 5)
graph.add_edge('t', 'y', 8)
graph.add_edge('t', 'z', -4)
graph.add_edge('y', 'z', 9)
graph.add_edge('y', 'x', -3)
graph.add_edge('z', 'x', -2)
graph.add_edge('x', 't', -2)

# Solve using Bellman-Ford
try:
    source = 's'
    shortest_paths = graph.bellman_ford(source)
    print(f"Shortest distances from source '{source}':")
    for vertex, distance in shortest_paths.items():
        print(f"Node {vertex}: {distance}")
except ValueError as e:
    print(e)
