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
