n = int(input("Enter a number: "))
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print("Reversed number is:", rev)

'''output:
Enter a number: 1234
Reversed number is: 4321
Enter a number: 100
Reversed number is: 1
Enter a number: 0
Reversed number is: 0
'''
