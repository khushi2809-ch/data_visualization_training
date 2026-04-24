import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [15, 25, 35, 45]

plt.plot(x, y1, label="Dataset 1")
plt.plot(x, y2, label="Dataset 2")

plt.legend()
plt.title("Comparison Plot")

plt.show()

'''output:
A line plot will be displayed showing two datasets with a legend to differentiate them.
'''
