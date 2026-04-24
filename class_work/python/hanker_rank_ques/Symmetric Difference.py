set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

result = set1.symmetric_difference(set2)
print(result)

'''output:
Enter numbers for set 1: 1 2 3
Enter numbers for set 2: 3 4 5
{1, 2, 4, 5}
Enter numbers for set 1: 1 2 3
Enter numbers for set 2: 4 5 6
{1, 2, 3, 4, 5, 6}
Enter numbers for set 1: 1 2 3
Enter numbers for set 2: 1 2 3
set()
Enter numbers for set 1: a b c
Enter numbers for set 2: c d e
{a, b, d, e}
'''