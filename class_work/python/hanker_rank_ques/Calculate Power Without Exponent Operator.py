base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

result = 1

for i in range(exp):
    result *= base

print(result)

'''output:
Enter base: 2
Enter exponent: 3
8
Enter base: 5
Enter exponent: 4
625
'''
