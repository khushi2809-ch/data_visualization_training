import numpy as np

arr = np.array([10, 20, 30, 40])

normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

print(normalized)

'''output:
[0.         0.33333333 0.66666667 1.        ]
'''
