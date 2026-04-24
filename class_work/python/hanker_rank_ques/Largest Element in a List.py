lst = list(map(int, input().split()))

largest = lst[0]

for num in lst:
    if num > largest:
        largest = num

print(largest)

'''output:
Enter numbers: 1 2 3 4 5
5
Enter numbers: 10 20 5 15
20
Enter numbers: -1 -5 -3 -2
-1
Enter numbers: 0 0 0 0
0
'''
