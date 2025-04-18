from collections import deque

# Breadth-First Search
def bfs(graph, start):
    visited = set()
    queue = deque([start])# brackets is so that it can loop through the queue as it becomes a queue
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node,end=" ")

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Input the graph
graph = {}
num_nodes = int(input("Enter the number of nodes: "))
for _ in range(num_nodes):
    node = input("Enter the node: ")
    neighbors = input(f"Enter the neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

# Input the starting node
start_node = input("Enter the starting node: ")

# Perform BFS
print("\nBFS Traversal:")
bfs(graph, start_node)# we are sending strings
print("\n graph is",graph)


