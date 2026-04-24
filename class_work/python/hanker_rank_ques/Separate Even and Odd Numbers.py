lst = list(map(int, input().split()))
even = []
odd = []

for num in lst:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even:", even)
print("Odd:", odd)

'''output:
Enter numbers: 1 2 3 4 5
Even: [2, 4]
Odd: [1, 3, 5]
Enter numbers: 10 15 20 25
Even: [10, 20]
Odd: [15, 25]
Enter numbers: -1 -2 -3 -4
Even: [-2, -4]
Odd: [-1, -3]
Enter numbers: 0 1 2 3
Even: [0, 2]
Odd: [1, 3]
'''
