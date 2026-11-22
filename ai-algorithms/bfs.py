import heapq

graphe = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 3)],
    'G': []
}
def bfs(graph, start, goal,way ):
    queue = [start]
    parents = {start: None}
    visited = set() 
    while queue:
       current_node = queue.pop(0) 
       if current_node in visited:
           continue
       visited.add(current_node)
       if current_node == goal:
              path = []
              while current_node is not None:
                    path.append(current_node)
                    current_node = parents[current_node]  
              way.extend(reversed(path))
              return True   
       for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                parents[neighbor] = current_node


    return None
start_node = 'A'
goal_node = 'G'
way = []
result = bfs(graphe, start_node, goal_node ,way)
if result:
    print(f"Il existe un chemin de {start_node} à {goal_node}.")
    print(f"Le chemin est: {way},and le cout est: {sum(w for i in range(len(way)-1) for n, w in graphe[way[i]] if n == way[i+1])}.")
        
