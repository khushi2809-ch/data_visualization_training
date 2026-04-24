lst = list(map(int, input().split()))
rev = []

for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])

print(rev)

'''output:
Enter numbers: 1 2 3 4 5
[5, 4, 3, 2, 1]
Enter numbers: 10 20 30
[30, 20, 10]
Enter numbers: -1 -2 -3
[-3, -2, -1]
Enter numbers: 0 0 0
[0, 0, 0]
'''
