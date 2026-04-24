n = int(input("Enter a number: "))
i = 2
total = 0

while i <= n:
    total += i
    i += 2

print("total:", total)

'''output:
Enter a number: 10
total: 30
Enter a number: 15
total: 56
Enter a number: 1
total: 0
'''