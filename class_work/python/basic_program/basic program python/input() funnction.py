# input() of data by user function 
name=input("enter your name")

principal=float(input (" enter the principal(in rupees)"))
rate=float(input("enter the rate of interest(in %):"))
time = float(input("Enter Time (in years): "))
simple_interest = (principal * rate * time) / 100
print("\n----- Result -----")
print("Principal Amount :", principal)
print("Rate of Interest :", rate)
print("Time (years)     :", time)
print("Simple Interest  :", round(simple_interest, 2))
