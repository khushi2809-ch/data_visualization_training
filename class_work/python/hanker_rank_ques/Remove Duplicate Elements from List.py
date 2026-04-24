lst = list(map(int, input().split()))
result = []

for num in lst:
    if num not in result:
        result.append(num)

print(result)

'''output:
Enter numbers: 1 2 3 2 4 1
[1, 2, 3, 4]
Enter numbers: 5 6 5 7 8 6
[5, 6, 7, 8]
Enter numbers: 1 1 1 1
[1]         
Enter numbers: 0 0 0 0
[0]
'''
