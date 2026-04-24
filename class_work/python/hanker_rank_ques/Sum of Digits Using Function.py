def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

n = int(input())
print(sum_digits(n))
'''output:
Enter a number: 1234
10
Enter a number: 0
0
'''
