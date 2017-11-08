import numpy as np

prim_graph = {
    0: {1:8, 2:9, 3:11},
    1: {0:8, 4:10},
    2: {0:9, 3:13, 4:5, 6:12},
    3: {0:11, 2:13, 5:8},
    4: {1:10, 2:5},
    5: {3:8, 6:7},
    6: {2:12, 5:7}
}

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
        
        
# prim3: https://www.ics.uci.edu/~eppstein/161/python/prim.py
        
        
       