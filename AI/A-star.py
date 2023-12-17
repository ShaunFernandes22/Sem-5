graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)]
}

def getNeighbors(v):
    if v in graph_nodes:
        return graph_nodes[v]
    else:
        return None

heuristic = {
    'A': 11,
    'B': 6, 
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0
}

def aStar(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {}
    parent = {}
    g[start_node] = 0
    parent[start_node] = start_node

    while (len(open_set) > 0):
        n = None
        for v in open_set:
            if n == None or g[v] + heuristic[v] < g[n] + heuristic[n]:
                n = v

        if n == goal_node or graph_nodes[n] == None:    
            pass
        else:
            for (m, weight) in getNeighbors(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    g[m] = g[n] + weight
                    parent[m] = n

                else:
                    if (g[m] > g[n] + weight):
                        g[m] = g[n] + weight
                        parent[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print("Path does not exist !")
            return None
        if n == stop_node:
            path = []

            while parent[n] != n:
                path.append(n)
                n = parent[n]
            path.append(start_node)
            path.reverse()
            print(f"The found path is {path}")
            return path
        
        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist")
    return None

start_node = input("Enter start node : ")
goal_node = input("Enter goal node : ")
aStar(start_node, goal_node)
