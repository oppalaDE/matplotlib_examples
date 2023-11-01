import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([2, 1, 4, 8])

# Draw vertical bars
plt.bar(x, y, color="orange", width=0.5)
plt.show()

# Draw horizontal bars
plt.barh(x, y, color="red", height=0.5)
x2 = np.array(["E", "F"])
y2 = np.array([6, 3])
plt.barh(x2, y2, color="brown", height=0.8)
plt.show()
