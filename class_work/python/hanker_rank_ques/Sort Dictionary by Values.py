d = eval(input())

sorted_items = sorted(d.items(), key=lambda x: x[1])

for key, value in sorted_items:
    print(key, value)

'''output:
Enter a dictionary: {'a': 3, 'b': 1, 'c': 2}
b 1
c 2
a 3
Enter a dictionary: {'x': 30, 'y': 10, 'z': 20}
y 10
z 20
x 30
'''