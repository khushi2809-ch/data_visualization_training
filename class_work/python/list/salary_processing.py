# Salary Processing System

# Step 1: Input salaries
salaries = []
n = int(input("Enter number of employees: "))

for i in range(n):
    sal = float(input(f"Enter salary of employee {i+1}: "))
    salaries.append(sal)

# Step 2: Remove salaries below minimum wage
min_wage = float(input("Enter minimum wage: "))
valid_salaries = []

for sal in salaries:
    if sal >= min_wage:
        valid_salaries.append(sal)

# Check if list is empty
if len(valid_salaries) == 0:
    print("No valid salaries available.")
else:
    # Step 3: Add 5% bonus if salary > 50000
    for i in range(len(valid_salaries)):
        if valid_salaries[i] > 50000:
            bonus = valid_salaries[i] * 0.05
            valid_salaries[i] += bonus

    # Step 4: Sort in descending order
    valid_salaries.sort(reverse=True)

    # Step 5: Display top 3 highest salaries
    print("\nProcessed Salaries (Descending):", valid_salaries)

    top_3 = valid_salaries[:3]
    print("Top 3 Highest Salaries:", top_3)
    '''output example:
Enter number of employees: 5
Enter salary of employee 1: 45000
Enter salary of employee 2: 55000
Enter salary of employee 3: 60000
Enter salary of employee 4: 40000
Enter salary of employee 5: 70000
Enter minimum wage: 45000
Processed Salaries (Descending): [73500.0, 63000.0, 47250.0]
Top 3 Highest Salaries: [73500.0, 63000.0, 47250.0]
    '''
    