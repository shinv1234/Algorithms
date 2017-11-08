import numpy as np

dfs_graph = {
    0: [1, 5, 7],
    1: [0, 2, 5],
    2: [1, 3, 4],
    3: [2, 4],
    4: [2, 3],
    5: [0, 1, 6, 7],
    6: [5],
    7: [0, 5]
}
         
dfs_graph2 = np.array([
    [0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0], 
    [0, 1, 0, 1, 1, 0, 0, 0], 
    [0, 0, 1, 0, 1, 0, 0, 0], 
    [0, 0, 1, 1, 0, 0, 0, 0], 
    [1, 1, 0, 0, 0, 0, 1, 1], 
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0]]
)

# Depth-First Search
def next_depth(graph, visited, vertex):
    visited[vertex] = 1
    print('vertex:', vertex, 'visited:', visited)
    for near_vertex in graph[vertex]:
        print('near_vertexs:', graph[vertex])
        if visited[near_vertex] == 0:
            next_depth(graph, visited, near_vertex)

def dfs4dict(graph, start):
    visited = dict() 
    for keys in graph.keys():
        visited[keys] = 0
    for vertex in graph.keys():
        if visited[vertex] == 0:
            next_depth(graph, visited, vertex)
    return visited

def next_depth2(graph, visited, vertex):
    visited[vertex] = 1
    print('vertex:', vertex, 'visited:', visited)
    possible_path = np.where(graph[vertex] == 1)[0].tolist()
    print('possible_path:', possible_path)
    for near_vertex in possible_path:
        print('near_vertexs:', near_vertex)
        if visited[near_vertex] == 0:
            next_depth2(graph, visited, near_vertex)

def dfs4matrix(graph, start):
    visited = dict() 
    for keys in range(graph.shape[0]):
        visited[keys] = 0
    for vertex in range(graph.shape[0]):
        if visited[vertex] == 0:
            next_depth2(graph, visited, vertex)
    return visited
