set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

result = set1.union(set2)
print(result)

'''output:
Enter numbers for set 1: 1 2 3
Enter numbers for set 2: 3 4 5
{1, 2, 3, 4, 5}
Enter numbers for set 1: 1 2 3
Enter numbers for set 2: 4 5 6
{1, 2, 3, 4, 5, 6}
Enter numbers for set 1: 1 2 3
Enter numbers for set 2: 1 2 3
{1, 2, 3}
Enter numbers for set 1: 1 2 3
Enter numbers for set 2: 4 5 6
{1, 2, 3, 4, 5, 6}
'''
