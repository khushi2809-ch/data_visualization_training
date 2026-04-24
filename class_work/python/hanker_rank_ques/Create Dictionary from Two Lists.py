keys = input().split()
values = list(map(int, input().split()))

d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]

print(d)

'''output:
Enter keys: a b c
Enter values: 1 2 3
{'a': 1, 'b': 2, 'c': 3}
Enter keys: x y z
Enter values: 10 20 30
{'x': 10, 'y': 20, 'z': 30}
'''
