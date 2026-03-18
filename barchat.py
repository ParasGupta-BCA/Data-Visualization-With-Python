import matplotlib
import matplotlib.pyplot as plt

plt.subplot(2,2,3)
avg_tip= data.groupby('sex')['tip'].mean()
plt.bar(avg_tip.index,avg_tip.values)
plt.title("Bar Chart: Avg Tip By Gender")
plt.xlabel("Gender")
plt.ylabel("Average Tip")