lst = list(map(int, input().split()))
k = int(input())

k = k % len(lst)
rotated = lst[k:] + lst[:k]

print(rotated)

'''output:
Enter numbers: 1 2 3 4 5
Enter K: 2
[3, 4, 5, 1, 2]
Enter numbers: 10 20 30 40
Enter K: 3
[40, 10, 20, 30]
Enter numbers: -1 -2 -3 -4
Enter K: 1
[-2, -3, -4, -1]
Enter numbers: 0 0 0 0
Enter K: 2
[0, 0, 0, 0]
'''
