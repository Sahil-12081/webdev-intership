from collections import defaultdict, deque

# Create undirected graph using adjacency list
graph = defaultdict(list)

# Take user input for edges
num_edges = int(input("Enter the number of edges in the graph: "))
print("Enter each edge in the format: node1 node2")

for _ in range(num_edges):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)  # Since it's an undirected graph

# DFS (Recursive)
def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# BFS (Iterative)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Start node input
start_node = input("Enter the starting node: ")

# Run DFS
print("\nDepth-First Search (DFS):")
visited_dfs = set()
dfs(visited_dfs, graph, start_node)

# Run BFS
print("\nBreadth-First Search (BFS):")
bfs(graph, start_node)
