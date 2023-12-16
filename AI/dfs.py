graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["G"],
    "D": [],
    "E": ["F"],
    "F": [],
    "G": []
}

def dfs(graph, visited, src, goal, depth):

    print(src, end=" ")
    visited.append(src)
    
    if src == goal:
        print()
        print("Goal node reached!")
        return  True

    for neighbor in graph[src]:
        if neighbor not in visited:
            
            if (dfs(graph, visited, neighbor, goal, depth+1) == True):
                return True

    return False

visited = []

src = input("Enter source node: ")
goal = input("Enter goal node: ")

if src not in graph or goal not in graph:
    print("Invalid source or goal node.")
else:
    dfs(graph, visited, src, goal, 0)
