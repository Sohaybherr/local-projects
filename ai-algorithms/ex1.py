import heapq
import matplotlib.pyplot as plt
import networkx as nx


graphe ={
    'A': [('C', 5), ('D', 5)],
    'C': [('H', 3),('F',2),('B', 3)],
    'D': [('C', 6),('E', 2)],
    'E': [('B', 5)],
    'F': [('G', 3)],
    'B': [('G', 4),('I', 5)],
    'H': [('I', 4)],
    'G': [('I', 3)],
    'I': []
}
def plot_graph(graph):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)
    pos = nx.spring_layout(G)
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()
def plot_path(graph, path):
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)
    pos = nx.spring_layout(G)
    edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    plt.show()    

def dfs(graph, start, goal, goalway,visited):
    if start not in visited:
        visited.add(start)
        goalway.append(start)
        if start == goal:
            return True
        sorted_neighbors = sorted(graph[start], key=lambda x: x[0])
        for neighbor, weight in sorted_neighbors:
                if neighbor not in visited:
                    if dfs(graph, neighbor, goal, goalway, visited):
                        return True
        goalway.pop()
    return False
def bfs(graph, start, goal, goalway):
    queue = [start]
    visited = set()
    parents = {start: None} 
    while queue:
        current_node = queue.pop(0)
        if current_node == goal:
                while current_node is not None:
                    goalway.append(current_node)
                    current_node = parents[current_node]
                goalway.reverse()     
                return True
        
        if current_node not in visited:
            visited.add(current_node)
            for neighbor, weight in sorted(graph[current_node], key=lambda x: x[0]):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    parents[neighbor] = current_node
    return False
def mincostpath(graph, start, goal, goalway):
    queue = [(0, start)]
    visited = set()
    distances = {start: 0}
    parents = {start: None}
    while queue:
        current_cost, current_node = heapq.heappop(queue)
        if current_node == goal:
                while current_node is not None:
                    goalway.append(current_node)
                    current_node = parents[current_node]
                goalway.reverse()
                return current_cost
        if current_node not in visited:
            visited.add(current_node)
            for neighbor, weight in graph[current_node]:
                new_cost = current_cost + weight
                if neighbor not in distances or new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    heapq.heappush(queue, (new_cost, neighbor))
                    parents[neighbor] = current_node
    return False
def astar(graph, h, start, goal):
    queue = [(h[start], 0, start)]   # (f, g, node)
    parents = {start: None}
    costs = {start: 0}

    while queue:
        f, g, current = heapq.heappop(queue)

        if current == goal:
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parents[node]
            path.reverse()
            return path, g

        for neighbor, weight in graph[current]:
            new_g = g + weight

            if neighbor not in costs or new_g < costs[neighbor]:
                costs[neighbor] = new_g
                parents[neighbor] = current
                new_f = new_g + h[neighbor]
                heapq.heappush(queue, (new_f, new_g, neighbor))

    return None, float("inf") 
import heapq

def gloutonne(graph, h, start, goal):
    queue = [(h[start], start)]   # (h, node)
    visited = set()
    parents = {start: None}

    while queue:
        _, current = heapq.heappop(queue)

        if current == goal:
            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parents[node]
            path.reverse()

            cost = 0
            for i in range(len(path) - 1):
                for neighbor, weight in graph[path[i]]:
                    if neighbor == path[i + 1]:
                        cost += weight
                        break

            return path, cost

        if current not in visited:
            visited.add(current)

            for neighbor, weight in graph[current]:
                if neighbor not in visited:
                    if neighbor not in parents:
                        parents[neighbor] = current
                    heapq.heappush(queue, (h[neighbor], neighbor))

    return None, float("inf")
                    


start_node = 'A'
goal_node = 'I'
goalway1 = []
visited = set()
allpaths = []
result = dfs(graphe, start_node, goal_node, goalway1, visited)
if result:
    print(f"Il existe un chemin de {start_node} à {goal_node}.")
    print(f"Le chemin est: {' -> '.join(goalway1)}.")
goalway2 = []
result2 = bfs(graphe, start_node, goal_node, goalway2)
if result2:
    print(f"Il existe un chemin de {start_node} à {goal_node}.")
    print(f"Le chemin est: {' -> '.join(goalway2)}")
goalway3 = []
result3 = mincostpath(graphe, start_node, goal_node, goalway3)
if result3:
    print(f"Le coût minimum de {start_node} à {goal_node} est: {result3}")
    print(f"Le chemin est: {' -> '.join(goalway3)}")
result4, cost4 = astar(graphe, {'A': 10, 'B': 4, 'C':5, 'D': 10, 'E': 10, 'F': 3, 'G': 3, 'H': 4, 'I': 0}, start_node, goal_node)    
print(f"Le chemin A* de {start_node} à {goal_node} est: {' -> '.join(result4)}")
print(f"Le coût A* est: {cost4}")
result5, cost5 = gloutonne(graphe, {'A': 10, 'B': 4, 'C':5, 'D': 10, 'E': 10, 'F': 3, 'G': 3, 'H': 4, 'I': 0}, start_node, goal_node)
print(f"Le chemin gloutonne de {start_node} à {goal_node} est: {' -> '.join(result5)}")
print(f"Le coût gloutonne est: {cost5}")
plot_graph(graphe)
plot_path(graphe, goalway1)
plot_path(graphe, goalway2)
plot_path(graphe, goalway3)
plot_path(graphe, result4)
plot_path(graphe, result5)