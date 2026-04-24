dict1 = eval(input())
dict2 = eval(input())

merged = {}

for key in dict1:
    merged[key] = dict1[key]

for key in dict2:
    merged[key] = dict2[key]

print(merged)

'''output:
Enter first dictionary: {'a': 1, 'b': 2}
Enter second dictionary: {'b': 3, 'c': 4}
{'a': 1, 'b': 3, 'c': 4}
Enter first dictionary: {'x': 10, 'y': 20}
Enter second dictionary: {'y': 30, 'z': 40}
{'x': 10, 'y': 30, 'z': 40}
Enter first dictionary: {'p': 5, 'q': 10}
Enter second dictionary: {'r': 15, 's': 20}
{'p': 5, 'q': 10, 'r': 15, 's': 20}
Enter first dictionary: {'a': 1, 'b': 2}
Enter second dictionary: {'a': 3, 'b': 4}
{'a': 3, 'b': 4}
'''
