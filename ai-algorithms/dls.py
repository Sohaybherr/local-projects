graphe = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}
def dls(graph, start, goal_node, depth,original_depth,allpaths,path):
    path.append(start)
    if start == goal_node:
        allpaths.append(path.copy())
        path.pop()
        return
    if depth == 0:
        path.pop()
        return
    for neighbor, weight in graph[start]:
        if neighbor not in path:
            dls(graph, neighbor, goal_node, depth - 1, original_depth, allpaths, path)
    path.pop()        
    

start_node = 'A'
goal_node = 'G'
max_depth = 3
visited = set()
path = []
allpaths = []
dls(graphe, start_node, goal_node, max_depth, max_depth, allpaths, path)
if allpaths:
    print(f"Il existe un chemin de {start_node} à {goal_node} avec une profondeur maximale de {max_depth}.")
    for p in allpaths:
        print(f"Le chemin est: {' -> '.join(p)}.")

else:
    print(f"Il n'existe pas de chemin de {start_node} à {goal_node} avec une profondeur maximale de {max_depth}.")    
