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

prim_graph = {
    0: {1:8, 2:9, 3:11},
    1: {0:8, 4:10},
    2: {0:9, 3:13, 4:5, 6:12},
    3: {0:11, 2:13, 5:8},
    4: {1:10, 2:5},
    5: {3:8, 6:7},
    6: {2:12, 5:7}
}

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


# prim(다시 확인하기)
def extract_min(full_vertexes, visited, cost):
    for vst in visited:
        cost[vst] = float('inf')
    print('cost:', cost)
    min_value = min(cost)
    min_value_vertex = cost.index(min_value)
    for nv in full_vertexes:
        if cost[nv] < min_value:
            min_value = cost[nv]
            min_value_vertex = nv
    return min_value_vertex

def prim4dict(graph, start):
    full_vertexes = {i for i in graph.keys()} # 모든 정점(set)
    visited = set() # 방문한 정점 목록(set)
    cost = [] # 현재 정점에서 주변 정점까지의 연결비용
    tree = {} # {정점:연결비용이 가장 적게 드는 이전 정점} 연결비용이 가장 적게 드는 간선을 저장
    for key in graph.keys(
        cost.append(float('inf')) # 연결비용 초기화
    cost[start] = 0 # 시작 정점의 연결비용을 0으로
    visited.add(start) # 방문한 정점목록에 시작정점을 입력
    while visited != full_vertexes:
        near_positions = graph[start] # 현 정점에서 방문 가능한 정점들(dict)
        print('near_positions:', near_positions)
        for np in near_positions:
            cost[np] = near_positions[np] # 현 정점에서 방문 가능한 정점들의 연결비용 갱신
        print('cost:', cost)
        position = extract_min(full_vertexes, visited, cost)
        visited.add(position)
        print('position:', position, 'visited:', visited)
        print('next_path:', graph[position].keys())
        for next_visit in graph[position].keys():
            condition1 =  next_visit in (full_vertexes - visited) # 
            condition2 = graph[position][next_visit] < cost[position]
            print('condition1:', condition1, 'condition2:', condition2)
            if condition1 and condition2:
                cost[next_visit] = graph[position][next_visit]
                tree[next_visit] = position
            print('tree:', tree, 'visited:', visited)
    return tree # ...

# https://jlmedina123.wordpress.com/2014/05/29/prims-algorithm-in-python/
# 확인하기
def popmin(pqueue):
    # A (ascending or min) priority queue keeps element with
    # lowest priority on top. So pop function pops out the element with
    # lowest value. It can be implemented as sorted or unsorted array
    # (dictionary in this case) or as a tree (lowest priority element is
    # root of tree)
    lowest = 1000
    keylowest = None
    for key in pqueue:
        if pqueue[key] < lowest:
            lowest = pqueue[key]
            keylowest = key
    del pqueue[keylowest]
    return keylowest
 
def prim(graph, root):
    pred = {} # pair {vertex: predecesor in MST}
    key = {}  # keep track of minimum weight for each vertex
    pqueue = {} # priority queue implemented as dictionary
 
    for v in graph:
        pred[v] = -1
        key[v] = 1000
    key[root] = 0
    for v in graph:
        pqueue[v] = key[v]
     
    while pqueue:
        u = popmin(pqueue)
        for v in graph[u]: # all neighbors of v
            if v in pqueue and graph[u][v] < key[v]:
                pred[v] = u
                key[v] = graph[u][v]
                pqueue[v] = graph[u][v]
    return pred, key, pqueue