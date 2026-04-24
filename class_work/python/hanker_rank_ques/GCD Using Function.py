def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input())
b = int(input())

print(gcd(a, b))

'''output:
Enter first number: 48
Enter second number: 18
6
Enter first number: 56
Enter second number: 98
14
'''
