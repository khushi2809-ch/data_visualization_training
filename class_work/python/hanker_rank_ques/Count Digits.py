n = int(input("Enter a number: "))
count = 0

while n > 0:
    count += 1
    n //= 10

print("count of digits is:", count)

'''output:
Enter a number: 1234
count of digits is: 4
Enter a number: 100
count of digits is: 3
Enter a number: 0
count of digits is: 1
'''