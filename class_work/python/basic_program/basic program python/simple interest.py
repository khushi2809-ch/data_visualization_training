# Program to calculate Simple Interest(9/10)

P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of interest: "))
T = float(input("Enter Time (in years): "))

SI = (P * R * T) / 100

print("Simple Interest is:", SI)

# Program to Calculate Simple Interest(10/10)

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))

simple_interest = (principal * rate * time) / 100

print("\n----- Result -----")
print("Principal Amount :", principal)
print("Rate of Interest :", rate)
print("Time (years)     :", time)
print("Simple Interest  :", round(simple_interest, 2))
