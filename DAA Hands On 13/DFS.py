from collections import defaultdict

def depth_first_search(edges, start):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = set()

    def dfs(v):
        if v not in visited:
            print(v, end=' ')
            visited.add(v)
            for neighbor in graph[v]:
                dfs(neighbor)

    dfs(start)
    print()

# Define edges for DFS example
edges_dfs = [
    ("u", "v"),
    ("u", "x"),
    ("v", "y"),
    ("y", "x"),
    ("x", "v"),
    ("w", "z"),
    ("w", "y"),
    ("z", "z")  # self-loop
]

print("Depth-First Search from 'u':")
depth_first_search(edges_dfs, 'u')
