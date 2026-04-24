d = eval(input())
key = input()

if key in d:
    d.pop(key)

print(d)

'''output:
Enter a dictionary: {'a': 1, 'b': 2, 'c': 3}
Enter key to remove: b
{'a': 1, 'c': 3}
Enter a dictionary: {'x': 10, 'y': 20, 'z': 30}
Enter key to remove: y
{'x': 10, 'z': 30}
Enter a dictionary: {'p': 5, 'q': 10, 'r': 15}
Enter key to remove: s
{'p': 5, 'q': 10, 'r': 15}
'''
