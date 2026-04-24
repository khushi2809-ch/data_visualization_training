n = int(input("Enter a number: "))

a, b = 0, 1
count = 0

while count < n:
    print(a)
    a, b = b, a + b
    count += 1
'''output:
Enter a number: 10
0
1
1
2
3
5
8
13
21
34
'''