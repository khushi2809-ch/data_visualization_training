n = int(input("Enter a number: "))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("Factorial of", n, "is", fact)

'''output:
Enter a number: 5
Factorial of 5 is 120
Enter a number: 0
Factorial of 0 is 1
Enter a number: 1
Factorial of 1 is 1
'''
