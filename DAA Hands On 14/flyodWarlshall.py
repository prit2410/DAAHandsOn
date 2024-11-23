def floyd_warshall(graph):
    # Initialize distances as infinity
    nodes = list(graph.keys())
    node_indices = {node: idx for idx, node in enumerate(nodes)}
    n = len(nodes)

    # Initialize distance and next_node matrices
    distances = [[float('inf')] * n for _ in range(n)]
    next_node = [[None] * n for _ in range(n)]

    # Distance to self is 0
    for i in range(n):
        distances[i][i] = 0

    # Add edges to the distance matrix
    for u in graph:
        for v, w in graph[u]:
            i, j = node_indices[u], node_indices[v]
            distances[i][j] = w
            next_node[i][j] = v

    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    next_node[i][j] = next_node[i][k]

    return distances, next_node, nodes

# Print matrix
def print_matrix(matrix, nodes):
    print("   ", "  ".join(nodes))
    for i, row in enumerate(matrix):
        print(f"{nodes[i]:<3}", "  ".join(f"{val if val != float('inf') else '∞':<3}" for val in row))

# Graph definition
graph = {
    's': [('t', 3), ('y', 5)],
    't': [('y', 2), ('x', 6)],
    'y': [('t', 1), ('x', 4), ('z', 6)],
    'x': [('z', 2)],
    'z': [('s', 3), ('x', 7)]
}

# Run Floyd-Warshall algorithm
distances, next_node, nodes = floyd_warshall(graph)

# Display results
print("Distance matrix:")
print_matrix(distances, nodes)
