lst = list(map(int, input().split()))

smallest = lst[0]

for num in lst:
    if num < smallest:
        smallest = num

print(smallest)

'''output:
Enter numbers: 1 2 3 4 5
1
Enter numbers: 10 20 5 15
5
Enter numbers: -1 -5 -3 -2
-5
Enter numbers: 0 0 0 0
0
'''
