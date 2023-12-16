graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E', 'F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

source = input("Enter the source node : ")
goal = input("Enter the goal node : ")

def bfs(graph, source, goal):
    visited = []
    queue = []
    
    visited.append(source)
    queue.append(source)

    
    while queue:
        current_node = queue.pop(0)
        print(current_node, end = ' ')
        
        if current_node == goal:
            print()
            print("Goal node reached")
            break
        
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
                
    return         
            
if (source not in graph) or (goal not in graph):
    print("Enter valid nodes")
else:
    bfs(graph, source, goal)
