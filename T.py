import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("Hospital_Data_Visualization.csv")

# Histogram with 5 bins
plt.figure()
plt.hist(df["Revenue"], bins=5)
plt.title("Histogram of Revenue (5 Bins)")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()

# Histogram with 8 bins
plt.figure()
plt.hist(df["Revenue"], bins=8)
plt.title("Histogram of Revenue (8 Bins)")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()