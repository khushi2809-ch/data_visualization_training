import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

arr[arr % 2 != 0] = -1

print(arr)

'''output:
[-1  2 -1  4 -1  6]
'''
