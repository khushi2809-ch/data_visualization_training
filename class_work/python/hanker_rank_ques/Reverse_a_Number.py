n = int(input("Enter a number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print("reverse of the number is:", rev)

'''output:
Enter a number: 1234
reverse of the number is: 4321
'''