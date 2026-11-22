graphe = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}

def dfspaths(graph, start, goal, goalway,allpaths):
    goalway.append(start)
    if start == goal:
        allpaths.append((goalway).copy()) 
    for neighbor, weight in graph[start]:
        if neighbor not in goalway:
            dfspaths(graph, neighbor, goal, goalway, allpaths)        
    goalway.pop()
visited = set()
start_node = 'A'
goal_node = 'G'
goalway = []
allpaths = []
dfspaths(graphe, start_node, goal_node, goalway, allpaths)
if allpaths:
    print(f"Il existe un chemin de {start_node} à {goal_node}.")
    for path in allpaths:
        print(f"Le chemin est: {' -> '.join(path)}.")
else:
    print(f"Il n'existe pas de chemin de {start_node} à {goal_node}.")