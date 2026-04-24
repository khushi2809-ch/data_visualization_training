def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

lst = list(map(int, input().split()))
print(unique_list(lst))

'''output:
Enter numbers: 1 2 3 2 4 1
[1, 2, 3, 4]
Enter numbers: 5 6 5 7 8 6
[5, 6, 7, 8]
'''
