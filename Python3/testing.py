# heap sort 
# Why cannot execute..;;
def heapify(lst, k, lst_size):
    left = 2*k
    right = 2*k+1
    print('k', k, 'left', left, 'right', right)
    # print(lst[left], lst[right])
    if right <= lst_size:
        if lst[left] < lst[right]:
            smaller = left
        else:
            smaller = right
    elif left <= lst_size:
        smaller = left
    else:
        return lst
    #print('smaller', smaller, 'k', k)
    #print(lst[smaller], lst[k])
    if lst[smaller] < lst[k]:
        print('lst[smaller] < lst[k]', 'smaller, ', smaller)
        smaller_element = lst[smaller]
        lst[smaller] = lst[k]
        lst[k] = smaller_element
        # heapify(lst, smaller, lst_size)
    print('lst', lst)

def build_heap(lst):
    lst_size = len(lst)
    for i in range((lst_size//2)-1, -1, -1):
        heapify(lst, i, lst_size)
    return lst



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


def select(lst, i):
    if len(lst) <= 1:
        print(lst[0])
        return lst[0]
    changed_lst, comparison_idx = partition(lst)
    # print('i:', i, 'lst:',lst ,'changed_lst:', changed_lst,'comparison_idx:' , comparison_idx)
    if i < comparison_idx:
        select(changed_lst[:comparison_idx], i)
    elif i > comparison_idx:
        select(changed_lst[comparison_idx+1:], i-comparison_idx-1)
    elif i == comparison_idx:
        print(changed_lst[i])
        return changed_lst[i]