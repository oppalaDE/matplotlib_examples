import matplotlib.pyplot as plt
import numpy as np

# Draw points
x = np.array([5, 7, 8, 3, 5, 4, 6, 7, 5, 5, 6, 3, 4, 6])
y = np.array([30, 45, 72, 27, 33, 49, 37, 45, 27, 43, 34, 35, 25, 29])
plt.scatter(x, y)

# Draw points with red color
x = np.array([3, 7, 10, 4, 7, 2, 3, 6, 6, 5])
y = np.array([22, 40, 75, 43, 61, 31, 34, 37, 32, 40])
plt.scatter(x, y, c="red")

# Draw transparent points with multiple colors and different sizes
x = np.array([3, 5, 7])
y = np.array([36, 34, 40])
colors = np.array(["green", "orange", "magenta"])
sizes = np.array([1500, 1200, 2300])
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
plt.show()

# Draw points with a colormap (Reference: https://matplotlib.org/stable/users/explain/colors/colormaps.html)
x = np.concatenate((np.random.randint(60, size=(200)), np.random.randint(40, 100, size=(200))))
y = np.concatenate((np.random.randint(60, size=(200)), np.random.randint(40, 100, size=(200))))
colors = [x[i] if x[i] > y[i] else y[i] for i in range(400)]
plt.scatter(x, y, c=colors, cmap='plasma')
plt.colorbar()
plt.show()
