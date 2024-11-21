def floyd_warshall(graph):
    # Number of vertices in the graph
    vertices = len(graph)

    # Initialize the distance and predecessor matrices
    dist = [[float('inf')] * vertices for _ in range(vertices)]
    pred = [[None] * vertices for _ in range(vertices)]

    # Set initial distances and predecessors
    for i in range(vertices):
        for j in range(vertices):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != float('inf'):
                dist[i][j] = graph[i][j]
                pred[i][j] = i + 1  # Store the predecessor (1-indexed)

    # Floyd-Warshall Algorithm
    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred


# Define the input graph as an adjacency matrix
# Use float('inf') to represent no direct edge
graph = [
    [0, 3, 8, float('inf'), -4],
    [float('inf'), 0, float('inf'), 1, 7],
    [float('inf'), 4, 0, float('inf'), float('inf')],
    [2, float('inf'), -5, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), 6, 0]
]

# Solve using Floyd-Warshall algorithm
distances, predecessors = floyd_warshall(graph)

# Display results
print("Distance matrix (D^k):")
for row in distances:
    print(row)

print("\nPredecessor matrix (Π^k):")
for row in predecessors:
    print(row)
