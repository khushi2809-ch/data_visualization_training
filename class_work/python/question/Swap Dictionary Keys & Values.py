d = {"a": 1, "b": 2, "c": 3}

swapped = {}

for key, value in d.items():
    swapped[value] = key

print(swapped)

'''output:
{1: 'a', 2: 'b', 3: 'c'}
'''
