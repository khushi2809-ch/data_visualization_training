set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

result = set1.intersection(set2)
print(result)

'''output:
Enter numbers for set 1: 1 2 3
Enter numbers for set 2: 3 4 5
{3}
Enter numbers for set 1: 1 2 3
Enter numbers for set 2: 4 5 6
set()
Enter numbers for set 1: 1 2 3
Enter numbers for set 2: 1 2 3
{1, 2, 3}
Enter numbers for set 1: 1 2 3
Enter numbers for set 2: 4 5 6
set()
'''
