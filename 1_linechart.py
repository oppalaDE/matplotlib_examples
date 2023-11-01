import matplotlib.pyplot as plt
import numpy as np

# Draw points connected with a line
x_points = np.array([0, 6, 8])
y_points = np.array([0, 250, 200])
plt.plot(x_points, y_points) # (blue)

# Draw line with default x points
y_points = np.array([50, 150, 300, 450, 500, 600])
plt.plot(y_points) # (orange)

# Draw line with marker points (Marker reference: https://www.w3schools.com/python/matplotlib_markers.asp)
# Marker style (marker), Marker size (ms), Marker face color (mfc), Marker edge color (mec)
# Line style (ls), Line width (lw), Line color (c)
x_points = np.array([5, 6, 7, 8])
y_points = np.array([50, 100, 200, 400])
plt.plot(x_points, y_points,
         marker="P", ms=10, mfc="black", mec="red",
         ls="dotted", lw=7, c="magenta") # User html color names or hex color code
# Shorthand: Format string (marker|line|color)
x_points = np.array([3, 5])
y_points = np.array([300, 500])
plt.plot(x_points, y_points, 'o:k') # circle|dotted|black

# Draw points without a line
x_points = np.array([5, 6])
y_points = np.array([150, 260])
plt.plot(x_points, y_points, marker='o', ls='') # (green)

plt.show()
