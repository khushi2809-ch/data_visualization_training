import matplotlib.pyplot as plt

categories = ["Food", "Rent", "Travel", "Shopping"]
values = [30, 40, 15, 15]

plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.title("Expense Distribution")

plt.show()

'''output:
A pie chart will be displayed showing the distribution of expenses across different categories.
'''
