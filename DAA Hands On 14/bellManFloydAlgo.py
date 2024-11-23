def bellman_ford(graph, start):
    # Initialize distances to all vertices as infinity and the start node as 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Dictionary to store the shortest path
    previous_nodes = {node: None for node in graph}

    # Flatten the graph edges into a list of (source, destination, weight)
    edges = [(u, v, w) for u in graph for v, w in graph[u]]

    # Relax edges |V| - 1 times
    for _ in range(len(graph) - 1):
        for u, v, w in edges:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                previous_nodes[v] = u

    # Check for negative weight cycles
    for u, v, w in edges:
        if distances[u] + w < distances[v]:
            raise ValueError("Graph contains a negative weight cycle")

    return distances, previous_nodes

# Graph definition
graph = {
    's': [('t', 3), ('y', 5)],
    't': [('y', 2), ('x', 6)],
    'y': [('t', 1), ('x', 4), ('z', 6)],
    'x': [('z', 2)],
    'z': [('s', 3), ('x', 7)]
}

# Run Bellman-Ford algorithm from source node 's'
try:
    distances, previous_nodes = bellman_ford(graph, 's')

    # Display results
    print("Shortest distances from source 's':")
    for node, distance in distances.items():
        print(f"{node}: {distance}")

    print("\nShortest paths from source 's':")
    for node in previous_nodes:
        path = []
        current = node
        while current is not None:
            path.insert(0, current)
            current = previous_nodes[current]
        print(f"Path to {node}: {' -> '.join(path)}")
except ValueError as e:
    print(e)
