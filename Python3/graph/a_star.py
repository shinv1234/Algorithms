a_star_graph = {
    0:{1:20},
    1:{4:17},
    2:{0:10, 1:17, 3:30, 4:25, 5:23},
    3:{0:19, 6:24},
    4:{7:25, 8:39},
    5:{3:16, 4:28, 6:18},
    6:{9:20},
    7:{8:29},
    8:{5:20, 9:28},
    9:{7:40}
}

a_star_h = {0:61, 1:68, 2:52, 3:30, 4:25, 5:34, 6:19, 7:39, 8:19, 9:0}

def extract_min(queue, f):
    q_f_dict = {v:c for v, c in zip(queue, f)}
    return min(q_f_dict, key=q_f_dict.get)

def a_star(graph, esti_dist, start, goal):
    if start == goal:
        raise Exception('Start == Goal')
    queue = [i for i in graph]
    halfway_path = [float('inf') for i in queue]
    residual_path = [float('inf') for i in queue]
    dist = [i for i in esti_dist]
    prev = dict()
    halfway_path[start] = 0
    residual_path[start] = dist[start]
    while len(queue) != 0:
        u = delete_min(queue, residual_path)
        # print(u)
        del queue[queue.index(u)]
        if u == goal:
            return prev
        else:
            for v in graph[u]:
                # print('u:',u, 'v:', v)
                cond0 = v in queue
                cond1 = halfway_path[u] + graph[u][v] < halfway_path[v]
                if cond0 and cond1:
                    halfway_path[v] = halfway_path[u] + graph[u][v]
                    prev[v] = u
                    residual_path[v] = halfway_path[v] + dist[v]
                    # print('halfway_path:', halfway_path, 'residual_path:', residual_path)
    return prev
