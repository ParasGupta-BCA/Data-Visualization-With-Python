import matplotlib.pyplot as plt

x=[0,2,4,6,8]
y=[0,4,16,36,64]

fig, ax=plt.subplot()
ax.plot(x,y,marker='O',label="Data Points")

ax.set_title("Basic Components of Matplotlib Figure")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")

plt.show()