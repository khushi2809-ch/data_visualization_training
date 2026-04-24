import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 50, 30, 20, 40]

plt.scatter(x, y)

max_y = max(y)
max_x = x[y.index(max_y)]

plt.scatter(max_x, max_y)

plt.title("Scatter Plot")

plt.show()

'''output:
A scatter plot will be displayed showing the relationship between x and y values, with the maximum y value highlighted.
'''
