graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'H'],
    'E': ['B', 'I'],
    'F': ['C'],
    'G': ['C'],
    'H': ['D'],
    'I': ['E']
}
def iddfs(graph, start, goal):
    def dfs(node, depth, visited, path, traversal_order):
        traversal_order.append(node)  

        if node == goal:
            return path + [node] 
        
        if depth == 0:
            return None
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                result = dfs(neighbor, depth - 1, visited.copy(), path + [node], traversal_order)
                if result:
                    return result
        
        return None
    for depth in range(len(graph) + 1):
        traversal_order = []  
        path = dfs(start, depth, set(), [], traversal_order)
        if path:
            print(f"Path found at depth {depth}")
            print(f"Traversal order for this depth: {' -> '.join(traversal_order)}")
            return traversal_order
    return None
start = 'A'
goal = 'G'
traversal_order = iddfs(graph, start, goal)
if traversal_order:
    print(f"\nFinal IDDFS Traversal Order: {' -> '.join(traversal_order)}")
else:
    print("\nNo path found.")
