# Importing relevant modules
import matplotlib.pyplot as plt


# Plotting Graphs in Python

# # Very basic plot
# x = [1, 3, 5, 10]   # This is what we are plotting
# plt.plot(x)
# plt.show()  # This shows what we are plotting

# x = [1, 3, 5, 10]
# y = [7, 12, 21, 25]
# plt.plot(x, y)
# plt.show()

# Let's plot a nicer plt
# Line 1 - Points
x = [3, 9, 14]
y = [2, 7, 38]
plt.plot(x, y, c="red", linewidth=2, label="line 1")

x2 = [1, 15, 18]
y2 = [0, 3, 12]
plt.plot(x2, y2, c="blue", linewidth=2, label="line 2",
         linestyle="dashed", marker='s', markerfacecolor="orange",
         markersize=5)

# Label the axis and title
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Two lines")

# Show legend on the plot
plt.legend()

# Axis Limits
plt.ylim(1, 10)
plt.xlim(1, 50)

# Get Python to show the plot
plt.show()




