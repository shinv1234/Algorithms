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