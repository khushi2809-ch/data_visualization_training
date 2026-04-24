lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

common = []

for num in lst1:
    if num in lst2 and num not in common:
        common.append(num)

print(common)

'''output:
Enter first list: 1 2 3
Enter second list: 3 4 5
[3]
Enter first list: 10 20 30
Enter second list: 20 40 50
[20]
Enter first list: -1 -2 -3
Enter second list: -3 -4 -5
[-3]
Enter first list: 0 0 0
Enter second list: 0 0 0
[0]
'''
