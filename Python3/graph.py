import numpy as np

bfs_graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 3, 4],
    3: [0, 2, 5, 6],
    4: [2],
    5: [3, 6],
    6: [3, 5, 7],
    7: [5, 6]
}
         
bfs_graph2 = np.array(
    [[0, 1, 1, 1, 0, 0, 0, 0], 
     [1, 0, 1, 0, 0, 0, 0, 0],
     [1, 1, 0, 1, 1, 0, 0, 0], 
     [1, 0, 1, 0, 0, 1, 1, 0], 
     [0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 1, 0],
     [0, 0, 0, 1, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 0, 1, 1]]
)

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

# Breath-First Search
def bfs4dict(graph, start):
    visited = dict() 
    for keys in graph.keys():
        visited[keys] = 0
    visited[start] = 1
    queue = [start] # position의 대기열?
    while queue:
        position = queue.pop(0)
        possible_path = graph[position]
        print('position:', position, 'possible_path:', possible_path)
        for j in possible_path:
            if visited[j] == 0:
                visited[j] = 1
                queue.append(j)
                print('visited:', visited, 'queue:', queue) 
    return visited

def bfs4dict2(graph, start):
    visited = set()
    queue = [start]
    while queue:
        position = queue.pop(0)
        if position not in visited:
            visited.add(position)
            #print visited
            queue.extend(set(graph[position]) - visited)
            #print queue
    return visited

def bfs4matrix(graph, start):
    visited = dict() 
    for keys in range(graph.shape[0]):
        visited[keys] = 0
    visited[start] = 1
    queue = [start] # position의 대기열?
    while queue:
        position = queue.pop(0)
        possible_path = np.where(graph[position] == 1)[0].tolist()
        print('position:', position, 'possible_path:', possible_path)
        for j in possible_path:
            if visited[j] == 0:
                visited[j] = 1
                queue.append(j)
                print('visited:', visited, 'queue:', queue) 
    return visited

def bfs4matrix2(graph, start):
    visited = [] # 방문 여부
    queue = [start]
    while queue:
        position = queue.pop(0) # 현재 위치
        print('position:', position)
        if position not in visited: # 현재 위치가 방문 경험이 없는 경우
            visited.append(position)
            possible_path = np.where(graph[position] == 1)[0].tolist()
            print('possible_path:', possible_path, 'visited:', visited)
            queue.extend(set(possible_path) - set(visited))
            print('queue:', queue)
    return visited


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