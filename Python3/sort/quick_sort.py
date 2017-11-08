
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