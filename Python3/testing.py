# heap sort
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