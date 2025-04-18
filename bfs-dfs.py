from collections import deque

# --- BFS Function ---
def bfs(graph, start):
    visited = set()# <-- Fix: Initialize visited set here
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# --- DFS Function ---
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            # Push neighbors in reverse for proper order
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

# --- Input Section ---
graph = {}
num_nodes = int(input("Enter the number of nodes: "))
for _ in range(num_nodes):  # <-- Fix: use _ instead of missing variable
    node = input("Enter the node: ")
    neighbors = input(f"Enter the neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

# --- Start Traversals ---
start_node = input("Enter the starting node: ")

print("\nBFS Traversal:")
bfs(graph, start_node)

print("\nDFS Traversal:")
dfs(graph, start_node)
