import numpy as np
import matplotlib.pyplot as plt
data=np.random.randint(10,100,50)
plt.figure(figsize=(6,4))
plt.plot(data,color='blue',marker='o')
plt.title("Line Chart of Random Numbers")
plt.title("Index")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.show()