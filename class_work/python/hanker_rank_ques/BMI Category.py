weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

'''output:
Enter weight in kg: 70
Enter height in meters: 1.75
Normal
Enter weight in kg: 50
Enter height in meters: 1.75
Underweight
Enter weight in kg: 80
Enter height in meters: 1.75
Overweight
'''