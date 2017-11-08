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