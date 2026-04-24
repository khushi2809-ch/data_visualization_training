n = int(input("Enter the number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a)
    a, b = b, a + b

'''output:
Enter the number of terms: 10
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
