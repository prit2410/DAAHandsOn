def depth_first_search(graph, start):
    visited = set()

    def dfs(v):
        if v not in visited:
            print(v, end=' ')
            visited.add(v)
            for neighbor in graph[v]:
                dfs(neighbor)

    dfs(start)
    print()

# Example usage of Depth-First Search
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("Depth-First Search from 'A':")
depth_first_search(graph, 'A')
