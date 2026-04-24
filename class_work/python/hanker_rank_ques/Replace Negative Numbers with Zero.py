lst = list(map(int, input().split()))

for i in range(len(lst)):
    if lst[i] < 0:
        lst[i] = 0

print(lst)

'''output:
Enter numbers: 1 -2 3 -4 5
[1, 0, 3, 0, 5]
Enter numbers: -10 20 -30 40
[0, 20, 0, 40]
Enter numbers: -1 -2 -3
[0, 0, 0]
Enter numbers: 0 0 0
[0, 0, 0]
'''
