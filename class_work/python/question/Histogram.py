import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(1, 100, 50)

plt.hist(data)
plt.title("Histogram")

plt.show()

'''output:
A histogram will be displayed showing the distribution of the random data.
'''
