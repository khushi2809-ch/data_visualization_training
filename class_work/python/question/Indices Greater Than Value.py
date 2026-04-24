
import numpy as np

arr = np.array([10, 25, 30, 15, 5])

value = 20

indices = np.where(arr > value)

print(indices)

'''output:
(array([1, 2, 3]),)
'''
