import heapq
import matplotlib.pyplot as plt
import networkx as nx

graph={
    'A':[('C',4),('D',3)]
}
def draw(graphe):
    G=nx.Graph()
    for node,neighs in graphe.items:
        for neigh,weigh in neighs:
            G.add_edge(node,neigh,weight=weigh)
    pos=nx.spring_layout(G)
    edge_labels={(u,v):d['weigh']for u,v,d in G.edges(data=True)}
    nx.draw(G,pos,with_labels=True,node_color='blue',node_size=100)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    plt.show()        
def bfs(graph, start, goal,path):
    queue=[start]
    visited=set()
    parent={start:None}
    while queue:
        current_node= heapq.heappop(queue)
        if(current_node==goal):
            while parent[current_node]:
                path.append(current_node)
                current_node=parent[current_node]
            path.reverse()
            return True    
        if current_node not in visited:
            visited.add(current_node)
            for niegh,weigh in graph[current_node]:
                if niegh not in visited and niegh not in queue:
                    heapq.heappush(queue, niegh)
                    parent[niegh]=current_node
        return False 
def dfs(graph,start,goal,visietd,path):
    if start not in visietd:
        path.append(start)
        visietd.add(start)
        if(start==goal):
            return True
        for neigh,weigh in graph[start]:
            if neigh not in visietd:
                if dfs(graph,start,goal,visietd,path):
                      return True
        path.pop()
    return False
def uniform_cost(graph,start,goal,path):
    queue=[(0,start)]
    visited=set()
    parent={start:None}
    min_table={start:0}
    while queue:
        min_cost,current_node=heapq.heappop(queue)
        if(current_node==goal):
            while parent[current_node] is not None:
                path.append(current_node)
                current_node=parent[current_node]
            path.reverse()
            return True,min_cost
        if(current_node not in visited):
            visited.add(current_node)
            for neigh,weigh in graph[current_node]:
                new_cost= weigh+min_cost
                if neigh not in min_table or min_table[neigh]>new_cost:
                    heapq.heappush(queue,(new_cost,neigh))
                    parent[neigh]=current_node
                    min_table[neigh]=new_cost
    return False,None
def astar(graph,h,start,goal,path):
    queue=[(h[start],start)]
    visited=set()
    parent={start:None}
    g_table={start:0}
    while queue:
        min_cost,current_node=heapq.heappop(queue)
        g_cost=g_table[current_node]
        if(current_node==goal):
            while current_node is not None:
                path.append(current_node)
                current_node=parent[current_node]
            path.reverse()
            return True,min_cost
        if(current_node not in visited):
            visited.add(current_node)
            for neigh,weigh in graph[current_node]:
                new_cost= weigh+g_cost
                new_f= new_cost+h[neigh]
                if neigh not in g_table or g_table[neigh]>new_cost:
                    heapq.heappush(queue,(new_f,neigh))
                    parent[neigh]=current_node
                    g_table[neigh]=new_cost
    return False,None
def greedy(graph,h,start,goal,path):
    queue=[(h[start],start)]
    visited=set()
    parent={start:None}
    while queue:
        min_h,current_node=heapq.heappop(queue)
        if(current_node==goal):
            while current_node is not None:
                path.append(current_node)
                current_node=parent[current_node]
            path.reverse()
            cost=0
            for i in range(len(path)-1):
                for neigh,weigh in graph[path[i]]:
                    if neigh==path[i+1]:
                        cost+=weigh
                        break
        if(current_node not in visited):
            visited.add(current_node)
            for neigh,weigh in graph[current_node]:
                if neigh not in visited:
                    heapq.heappush(queue,(h[neigh],neigh))
                    parent[neigh]=current_node
    return False,None

def draw_path(graphe,path):
    G=nx.Graph()
    for node,neighs in graphe.items:
        for neigh,weigh in neighs:
            G.add_edge(node,neigh,weight=weigh)
    pos=nx.spring_layout(G)
    edeglabel={(u,v):d['weigh']for u,v,d in G.edges(data=True)}
    nx.draw(G,pos,with_labels=True,node_color='blue')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edeglabel)
    edge_list=list(zip[path,path[1:]])
    nx.draw_networkx_edges(G,pos,edgelist=edge_list,edge_color='red')
    plt.show()   


 
                     




           
       