p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time period: "))

amount = p * (1 + r/100) ** t
ci = amount - p
print("Compound Interest is:", ci)

'''output:
Enter principal amount: 1000
Enter rate of interest: 5
Enter time period: 2
Compound Interest is: 102.5
'''