import heapq


def dijkstra(graph, source):
    # Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    priority_queue = [(0, source)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip processing if the distance is not optimal
        if current_distance > distances[current_node]:
            continue

        # Update neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Define the graph as an adjacency list
graph = {
    's': {'t': 10, 'y': 5, 'x': 9},
    't': {'x': 1, 'z': 4},
    'y': {'t': 3, 'z': 2},
    'x': {'z': 6},
    'z': {}
}

# Compute shortest paths from source 's'
source = 's'
shortest_paths = dijkstra(graph, source)

# Print the results
print("Shortest distances from source '{}':".format(source))
for node, distance in shortest_paths.items():
    print(f"Node {node}: {distance}")
