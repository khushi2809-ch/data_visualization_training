def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

base = int(input())
exp = int(input())

print(power(base, exp))

'''output:
Enter base: 2
Enter exponent: 3
8
Enter base: 5
Enter exponent: 0
1
'''
