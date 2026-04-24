d = eval(input())
key = input()

if key in d:
    print("Exists")
else:
    print("Not Exists")

'''output:
Enter a dictionary: {'a': 1, 'b': 2, 'c': 3}
Enter key to check: b
Exists
Enter a dictionary: {'x': 10, 'y': 20, 'z': 30}
Enter key to check: y
Exists
Enter a dictionary: {'p': 5, 'q': 10, 'r': 15}
Enter key to check: s
Not Exists
'''
