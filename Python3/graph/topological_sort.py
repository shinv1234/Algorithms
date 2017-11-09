from collections import deque
 

def kahn_topsort(graph): # https://algocoding.wordpress.com/2015/04/05/topological-sorting-python/
    in_degree = { u : 0 for u in graph }     # determine in-degree 
    for u in graph:                          # of each node
        for v in graph[u]:
            in_degree[v] += 1
 
    Q = deque()                 # collect nodes with zero in-degree
    for u in in_degree:
        if in_degree[u] == 0:
            Q.appendleft(u)
 
    L = []     # list for order of nodes
     
    while Q:                
        u = Q.pop()          # choose node of zero in-degree
        L.append(u)          # and 'remove' it from graph
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                Q.appendleft(v)
 
    if len(L) == len(graph):
        return L
    else:                    # if there is a cycle,  
        return []            # then return an empty list
    

def dfs_ts(graph, visited, v, order_list):
    visited[v] = 1
    print('v:', v, 'visited[v]:', visited[v], 'graph[v]:', graph[v])
    for nv in graph[v]:
        print('nv:', nv, 'visited[nv]:', visited[nv])
        if visited[nv] == 0:
            dfs_ts(graph, visited, nv, order_list)
    order_list.insert(0, v)
    print('order_list:', order_list)
    
def topological_sort(graph):
    order_list = []
    visited = dict()
    for v in graph:
        visited[v] = 0
    for v in graph:
        if visited[v] == 0:
            dfs_ts(graph, visited, v, order_list)
    return order_list
