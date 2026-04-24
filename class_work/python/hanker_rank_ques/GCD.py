a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print(a)
'''output:
Enter first number: 48
Enter second number: 18
6
Enter first number: 56
Enter second number: 98
14
'''