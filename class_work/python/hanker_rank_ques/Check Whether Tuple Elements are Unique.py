t = tuple(map(int, input().split()))

if len(t) == len(set(t)):
    print("Unique")
else:
    print("Not Unique")


'''output:
Enter numbers: 1 2 3 4 5
Unique
Enter numbers: 1 2 3 4 5 1
Not Unique
Enter numbers: 10 20 30
Unique
'''