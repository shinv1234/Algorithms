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
