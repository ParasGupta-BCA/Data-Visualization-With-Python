import numpy as np
import matplotlib.pyplot as plt

# Generate random array of 50 integers between 1 and 100
data = np.random.randint(1, 101, 50)

# Create x-axis index
x = np.arange(1, 51)

# Set overall style
plt.style.use('seaborn-v0_8')

# Create a 2x2 subplot layout
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Visualization of Random Integer Array", fontsize=16, fontweight='bold')

# 1. Line Chart
axs[0, 0].plot(x, data, color='blue', marker='o', linestyle='-', linewidth=2)
axs[0, 0].set_title("Line Chart")
axs[0, 0].set_xlabel("Index")
axs[0, 0].set_ylabel("Value")
axs[0, 0].grid(True)

# 2. Scatter Plot
axs[0, 1].scatter(x, data, color='red', s=60, edgecolor='black')
axs[0, 1].set_title("Scatter Plot")
axs[0, 1].set_xlabel("Index")
axs[0, 1].set_ylabel("Value")
axs[0, 1].grid(True)

# 3. Histogram
axs[1, 0].hist(data, bins=10, color='green', edgecolor='black')
axs[1, 0].set_title("Histogram")
axs[1, 0].set_xlabel("Value Range")
axs[1, 0].set_ylabel("Frequency")

# 4. Box Plot
axs[1, 1].boxplot(data, patch_artist=True,
                  boxprops=dict(facecolor='purple'))
axs[1, 1].set_title("Box Plot")
axs[1, 1].set_ylabel("Values")

# Adjust lay out
  plt.                                       bbbbbbbbbb





tight_layo u t()
pl    t.show()