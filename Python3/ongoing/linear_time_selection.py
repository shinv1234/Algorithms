# select(Why cannot execute 'return'??)
def partition(lst):
    changed_lst = []
    comparison_element = lst[len(lst)-1]
    changed_lst.append(comparison_element)
    comparison_idx = 0
    for i in range(len(lst)-1):
        element = lst[i]
        if comparison_element > element:
            changed_lst.insert(0, element)
            comparison_idx += 1
        else:
            changed_lst.append(element)
    return changed_lst, comparison_idx


def linear_time_selection(lst, i):
    if len(lst) <= 1:
        print(lst[0])
        return lst[0]
    changed_lst, comparison_idx = partition(lst)
    # print('i:', i, 'lst:',lst ,'changed_lst:', changed_lst,'comparison_idx:' , comparison_idx)
    if i < comparison_idx:
        linear_time_selection(changed_lst[:comparison_idx], i)
    elif i > comparison_idx:
        linear_time_selection(changed_lst[comparison_idx+1:], i-comparison_idx-1)
    elif i == comparison_idx:
        print(changed_lst[i])
        return changed_lst[i]