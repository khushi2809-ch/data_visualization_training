a = int(input("enter the element a: "))
b = int(input("enter the element b: "))
c = int(input("enter the element c: "))

if a >= b and a >= c:
    print("largest number is:", a)
elif b >= a and b >= c:
    print("largest number is:", b)
else:
    print("largest number is:", c)

'''output:
enter the element a: 5
enter the element b: 10
enter the element c: 3
largest number is: 10
enter the element a: 7
enter the element b: 4
enter the element c: 9
largest number is: 9
enter the element a: 2
enter the element b: 6
enter the element c: 1
largest number is: 6
'''