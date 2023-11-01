import matplotlib.pyplot as plt

plt.subplot(2, 1, 1) # 2 rows, 1 column, first plot (top)
# Here can be added some chart data (linechart, piechart,...)
plt.title("My Chart 1")
plt.xlabel("My X-Axis")
plt.ylabel("My Y-Axis")
plt.grid()

plt.subplot(2, 1, 2) # 2 rows, 1 column, second plot (bottom)
# Here can be added some chart data (linechart, piechart, scatter...)
titleFont = { "family": "serif", "color": "darkblue", "size": 20, "weight": 700 }
axisFont = { "family": "serif", "color": "darkgreen", "size": 14, "weight": 600 }
plt.title("My Chart 2", fontdict=titleFont, loc="left")
plt.xlabel("My X-Axis", fontdict=axisFont, loc="right")
plt.ylabel("My Y-Axis", fontdict=axisFont, loc="top")
plt.grid(axis="x", c="red", ls="--", lw=2)

plt.show()
