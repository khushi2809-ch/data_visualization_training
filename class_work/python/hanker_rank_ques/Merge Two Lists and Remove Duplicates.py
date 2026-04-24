lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

merged = lst1 + lst2
result = []

for num in merged:
    if num not in result:
        result.append(num)

print(result)

'''output:
Enter first list: 1 2 3
Enter second list: 3 4 5
[1, 2, 3, 4, 5]
Enter first list: 10 20 30
Enter second list: 20 40 50
[10, 20, 30, 40, 50]
Enter first list: -1 -2 -3
Enter second list: -3 -4 -5
[-1, -2, -3, -4, -5]
Enter first list: 0 0 0
Enter second list: 0 0 0
[0]
'''
