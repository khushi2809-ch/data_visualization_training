set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

if set1.issubset(set2):
    print("Subset")
else:
    print("Not Subset")

'''output:
Enter numbers for set 1: 1 2 3
Enter numbers for set 2: 1 2 3 4 5
Subset
Enter numbers for set 1: 1 2 3
Enter numbers for set 2: 4 5 6
Not Subset
Enter numbers for set 1: 1 2 3
Enter numbers for set 2: 1 2 3
Subset
Enter numbers for set 1: 1 2 3
Enter numbers for set 2: 1 2 3 4 5
Subset
'''
