d = eval(input())

max_key = max(d, key=d.get)
print(max_key)

'''output:
Enter a dictionary: {'a': 3, 'b': 1, 'c': 2}
a
Enter a dictionary: {'x': 30, 'y': 10, 'z': 20}
x
'''
