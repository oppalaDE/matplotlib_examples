import matplotlib.pyplot as plt
import numpy as np

# Generate a normal (Gaussian) distribution array 300 values,
# where the center is around 175 with a spread of 10
x = np.random.normal(175, 10, 300)

# Draw a histogram
plt.hist(x)
plt.show()

# Draw a histogram where only the data between a value of 160 and 185 are grouped into 5 bins
plt.hist(x, bins=5, range=(160, 185))
plt.show()
