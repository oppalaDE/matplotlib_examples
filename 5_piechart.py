import matplotlib.pyplot as plt
import numpy as np

# Draw pie chart
x = np.array([35, 25, 25, 15, 20])
plt.pie(x)
plt.show()

# Draw pie chart with labels and legend, colors, startangle, explode, shadow and clockwise
labels = ["A", "B", "C", "D", "E"]
colors = ["darkgreen", "lightgreen", "blue", "red", "magenta"]
explode = [0.1, 0.1, 0, 0, 0]
plt.pie(x, labels=labels, colors=colors, startangle=90, explode=explode, shadow=True, counterclock=False)
plt.legend(title="Categories:")
plt.show()
