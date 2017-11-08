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