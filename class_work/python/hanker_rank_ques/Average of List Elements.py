lst = list(map(int, input().split()))
total = 0

for num in lst:
    total += num

average = total / len(lst)
print(average)

'''output:
Enter numbers: 1 2 3 4 5
3.0
Enter numbers: 10 20 30
20.0
Enter numbers: -1 -2 -3
-2.0
Enter numbers: 0 0 0
0.0
'''
