# selection_sort
def fnd_lgst_idx(lst, last):
    """
    
    """
    chngd_lst = lst[0:last+1]
    lgst_idx = 0
    for i in range(1, len(chngd_lst)):
        if chngd_lst[lgst_idx] < chngd_lst[i]:
            lgst_idx = i
    return lgst_idx

def selection_sort(lst):
    """
    
    """
    for last in range(len(lst) -1, 0, -1):
        last_elmt = lst[last]
        lgst_idx = fnd_lgst_idx(lst, last)
        lst[last] = lst[lgst_idx]
        lst[lgst_idx] = last_elmt
    return lst



# bubble_sort
def bubble_sort(lst):
    """
    
    """
    for last in range(len(lst)-1, 0, -1):
        for i in range(last):
            if lst[i] > lst[i+1]:
                large_elmt = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = large_elmt
    return lst



# insertion_sort
def insertion_sort(lst):
    """
    
    """
    for i in range(1, len(lst)):
        idx = i - 1
        isrt_elmt = lst[i]
        while idx >= 0 and isrt_elmt < lst[idx]:
            lst[idx + 1] = lst[idx]
            idx -= 1
        lst[idx+1] = isrt_elmt
    return lst



# merge_sort
def merge(left, right):
    """
    
    """
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
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

def merge_sort(list):
    """
    
    """
    ''' # merge_sort([2, 4, 1, 3]) '''
    if len(list) <= 1:
        return list
    
    mid = len(list) // 2    
    leftList = list[:mid]
    rightList = list[mid:]
    # print('leftList ', leftList)
    # print('rightList ', rightList)
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    # print('merged_leftList ', leftList)
    # print('merged_rightList ', rightList)
    lst = merge(leftList, rightList)
    # print('lst ', lst)
    return lst




# quick_sort
def partition(lst):
    """
    
    """
    changed_lst = []
    comparison_element = lst[-1]
    comparison_idx = 0
    changed_lst.append(comparison_element)
    for i in range(len(lst) - 1):
        if lst[i] < comparison_element:
            comparison_idx += 1
            changed_lst.insert(0,lst[i])
        else:
            changed_lst.append(lst[i])
    return changed_lst, comparison_idx

def quick_sort(lst):
    """
    
    """
    if len(lst) <= 1:
        return lst
    
    changed_lst, comparison_idx = partition(lst)
    left_lst = quick_sort(changed_lst[:comparison_idx])
    right_lst = quick_sort(changed_lst[comparison_idx:])
    return left_lst + right_lst