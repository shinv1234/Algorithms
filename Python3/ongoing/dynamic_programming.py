import numpy as np

# Pebble
"""
It will be updated so that it does not matter the size.
"""
def block_select(table, p, i):
    """
    When i column is placed in pattern p, the sum of the points on the i column.
    """
    if p == 3:
        return table[[0, 2], i].sum()
    else:
        return table[p, i]

def pattern_check(p, q):
    """
    Return Boolean whether p and q could be compatible.
    """
    return (set([p, q]) in [set([0, 1]), set([0, 2]), set([1, 2]), set([1, 3])])

def pebble(table, p, i):
    """
    table: 3-rows numpy array
    p: pattern
    i: column
    """
    if i == 0:
        return block_select(table, p, 0)
    else:
        max_value = float('-inf')
        for q in range(4):
            if pattern_check(p, q):
                tmp = pebble(table, q, i-1)
                if tmp > max_value:
                    max_value = tmp
        return max_value + block_select(table, p, i)
    
def pebble_dp(table, n): # In progress
    peb_array = np.zeros((4, table.shape[1]))
    peb_array_max = np.zeros((4, table.shape[1]))
    for p in range(4):
        peb_array[p, 0] = block_select(table, p, 0)
        peb_array_max[p, 0] = block_select(table, p, 0)
    for i in range(1, n):
        for p in range(4):
            peb_array[p, i] = block_select(table, p, i)
            '''peb_array_max[p, 0] = '''
    return peb_array_max


