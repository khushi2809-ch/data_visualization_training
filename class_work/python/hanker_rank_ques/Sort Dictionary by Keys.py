d = eval(input())

for key in sorted(d.keys()):
    print(key, d[key])


'''output:
Enter a dictionary: {'b': 2, 'a': 1, 'c': 3}
a 1
b 2
c 3
Enter a dictionary: {'x': 10, 'z': 30, 'y': 20}
x 10
y 20
z 30
Enter a dictionary: {'p': 5, 'r': 15, 'q': 10}
p 5
q 10
r 15
'''