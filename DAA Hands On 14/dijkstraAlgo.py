import heapq


def dijkstra(graph, start):
    # Priority queue to store (distance, node)
    pq = []
    heapq.heappush(pq, (0, start))

    # Distance dictionary to store the shortest distance to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Dictionary to store the shortest path
    previous_nodes = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If the current distance is greater than the stored distance, skip
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path is found, update distances and push to the queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes


# Graph definition
graph = {
    's': [('t', 3), ('y', 5)],
    't': [('y', 2), ('x', 6)],
    'y': [('t', 1), ('x', 4), ('z', 6)],
    'x': [('z', 2)],
    'z': [('s', 3), ('x', 7)]
}

# Run Dijkstra's algorithm from source node 's'
distances, previous_nodes = dijkstra(graph, 's')

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
