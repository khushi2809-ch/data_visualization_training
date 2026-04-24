a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

'''output:
Enter first side: 5
Enter second side: 5
Enter third side: 5
Equilateral
Enter first side: 5
Enter second side: 5
Enter third side: 3
Isosceles
'''