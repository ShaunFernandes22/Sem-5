graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["G"],
    "D": [],
    "E": ["F"],
    "F": [],
    "G": []
}

def dfid(graph, src, goal):
    
    limit = 0
    while True:
        visited = []
        if (dls(graph, visited, src, goal, 0, limit) == True):
            print(f"\nGoal node reached at level {limit}!", end='')
            break
        print(f"\t\t level", limit)
        limit += 1

    return


def dls(graph, visited, src, goal, depth, limit):

    if (depth > limit):
        return False

    print(src, end=' ')
    visited.append(src)

    if src == goal:
        return True
    
    for neighbor in graph[src]:
        if neighbor not in visited:

            if (dls(graph, visited, neighbor, goal, depth+1, limit) == True):
                return True            

    return False


src = input("Enter source node: ")
goal = input("Enter goal node: ")

if src not in graph or goal not in graph:
    print("Invalid source or goal node.")
else:
    dfid(graph, src, goal)
