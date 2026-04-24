lst = list(map(int, input().split()))

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print(lst)

'''output:
Enter numbers: 5 2 9 1 5
[1, 2, 5, 5, 9]
Enter numbers: 3 4 1 2
[1, 2, 3, 4]
Enter numbers: 10 9 8 7
[7, 8, 9, 10]
Enter numbers: 0 0 0 0  
[0, 0, 0, 0]
'''
