bellman_ford_graph = {
    0:{1:8, 2:9, 3:11},
    1:{4:10},
    2:{1:-15, 3:3, 4:1},
    3:{5:8, 6:8},
    4:{7:2},
    5:{6:7},
    6:{2:12, 7:5},
    7:{5:4},
}


def bellman_ford(graph, start):
    prev = dict() # {vertex: prev_vertex}
    cost = [float('inf') for i in graph]
    cost[start] = 0
    for i in range(len(graph) - 1):
        for v in graph:
            for nv in graph[v]:
                if (cost[v] + graph[v][nv]) < cost[nv]:
                    cost[nv] = cost[v] + graph[v][nv]
                    prev[nv] = v
    return prev