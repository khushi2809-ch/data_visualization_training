lst = list(map(int, input().split()))

largest = second = float('-inf')

for num in lst:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print(second)

'''output:
Enter numbers: 1 2 3 4 5
4
Enter numbers: 10 20 5 15
15
Enter numbers: -1 -5 -3 -2
-2
Enter numbers: 0 0 0 0
0
'''
