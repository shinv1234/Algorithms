dijkstra_graph = {
    0:{1:8, 2:9, 3:11},
    1:{4:10},
    2:{1:6, 3:3, 4:1},
    3:{5:8, 6:8},
    4:{7:2},
    5:{6:7},
    6:{2:12, 7:5},
    7:{5:4},
}

def extract_min(all_vtx, visited, cost):
    v_c_dict = {v:c for v, c in zip(all_vtx, cost)}
    for vst in visited:
        del v_c_dict[vst]
    return min(v_c_dict, key=v_c_dict.get)

def dijkstra(graph, start):
    all_vtx = [i for i in graph]
    visited = []
    prev = dict() # {vertex: prev_vertex}
    cost = [float('inf') for i in graph]
    cost[start] = 0
    while visited != all_vtx:
        min_v = extract_min(all_vtx, visited, cost)
        visited.append(min_v)
        visited.sort()
        non_visited = list(set(all_vtx) - set(visited))
        for nv in graph[min_v]:
            condition0 = nv in non_visited
            condition1 = graph[min_v][nv] < cost[nv]
            if condition0 and condition1:
                cost[nv] = cost[min_v] + graph[min_v][nv]
                prev[nv] = min_v
    return prev