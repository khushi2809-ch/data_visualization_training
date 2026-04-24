a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

greatest = a

if b > greatest:
    greatest = b
if c > greatest:
    greatest = c
if d > greatest:
    greatest = d

print("The greatest number is:", greatest)

'''output:
Enter first number: 10
Enter second number: 20
Enter third number: 5
Enter fourth number: 15
The greatest number is: 20
'''
