kruskal_graph2 = {
    0: {1:3, 2:9, 3:2},
    1: {0:3, 2:11, 4:8},
    2: {0:9, 1:11, 3:13, 4:12, 5:3, 6:7},
    3: {0:2, 2:13, 5:10},
    4: {1:8, 2:12, 6:15},
    5: {2:3, 3:10, 6:4},
    6: {2:7, 4:15, 5:4}
}

kruskal_graph2 = {
    0: {1:3, 2:9, 3:2},
    1: {0:3, 2:11, 4:8},
    2: {0:9, 1:11, 3:13, 4:12, 5:3, 6:7},
    3: {0:2, 2:13, 5:10},
    4: {1:8, 2:12, 6:15},
    5: {2:3, 3:10, 6:4},
    6: {2:7, 4:15, 5:4}
}

# 1
def init_vtx_set(graph):
    return [{i} for i in graph]

# 2
def merge4kruskal(left, right):
    """
    
    """
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0][1] <= right[0][1]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

def merge_sort4kruskal(list):
    """
    
    """
    if len(list) <= 1:
        return list
    
    mid = len(list) // 2    
    leftList = list[:mid]
    rightList = list[mid:]
    # print('leftList ', leftList)
    # print('rightList ', rightList)
    leftList = merge_sort4kruskal(leftList)
    rightList = merge_sort4kruskal(rightList)
    # print('merged_leftList ', leftList)
    # print('merged_rightList ', rightList)
    lst = merge4kruskal(leftList, rightList)
    # print('lst ', lst)
    return lst

def make_vtx_edg_list(graph):
    '''
    전체 그래프를 간선 목록으로 변환
    '''
    duplicated_list = []
    vtx_edg_list = []
    for i in graph:
        for j in graph[i]:
            duplicated_list.append([set((i, j)), graph[i][j]])
    for k in duplicated_list: # 중복제거
        if k not in vtx_edg_list:
            vtx_edg_list.append(k)
    del duplicated_list
    vtx_edg_list = merge_sort4kruskal(vtx_edg_list)
    return vtx_edg_list


# 5
def check_separated_vtx(vtx_edg, vtx_edg_list):
    for vel in vtx_edg_list:
        if vtx_edg.issubset(vel):
            return False
    return True

# 7
def return_subset(single_vtx, vtx_sets):
    for vtx in vtx_sets:
        if single_vtx.issubset(vtx):
            vtx_sets.remove(vtx)
            return vtx
    raise Exception('error!')

def merge_vtx(vtxes, vtx_sets):
    vtxes_list = [{i} for i in vtxes]
    condition0 = vtxes_list[0] in vtx_sets
    condition1 = vtxes_list[1] in vtx_sets
    if condition0 and condition1:
        vtx_sets.append(vtxes)
        vtx_sets.remove(vtxes_list[0])
        vtx_sets.remove(vtxes_list[1])
        return vtx_sets
    elif condition0 or condition1:
        if condition0:
            vtx_sets.remove(vtxes_list[0])
            vtx_set2 = return_subset(vtxes_list[1], vtx_sets)
            vtx_set2 = vtx_set2.union(vtxes_list[0])
            vtx_sets.append(vtx_set2)
            return vtx_sets
        if condition1:
            vtx_sets.remove(vtxes_list[1])
            vtx_set1 = return_subset(vtxes_list[0], vtx_sets)
            vtx_set1 = vtx_set1.union(vtxes_list[1])
            vtx_sets.append(vtx_set1)
            return vtx_sets
    else:
        vtx_set1 = return_subset(vtxes_list[0], vtx_sets)
        vtx_set2 = return_subset(vtxes_list[1], vtx_sets)
        vtx_sets.append(vtx_set1.union(vtx_set2))
        return vtx_sets
    
def kruskal4dict(graph):
    spanning_tree = []
    vtx_sets = init_vtx_set(graph)
    vtx_edg_list = make_vtx_edg_list(graph)
    n = len(vtx_sets)
    while len(spanning_tree) < n - 1:
        min_vtx_edg = vtx_edg_list.pop(0)
        if check_separated_vtx(min_vtx_edg[0], vtx_sets):
            spanning_tree.append(min_vtx_edg)
            vtx_sets = merge_vtx(min_vtx_edg[0], vtx_sets)
    return spanning_tree