import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
revenue = [200, 250, 300, 280, 350]

plt.plot(months, revenue)

plt.title("Monthly Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue")
plt.grid()

plt.show()

'''output:
A line plot will be displayed showing the monthly revenue with a title, labeled axes, and a grid for better readability.
'''
