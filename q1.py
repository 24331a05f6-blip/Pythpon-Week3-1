temps=[28,34,27,29,31,26,35]
print("list: ",temps)
import numpy as np
temp =np.array(temps)
print("np array: ",temp)
print("Temperature data:", temp)
print("Number of dimensions:", temp.ndim)
print("Minimum temperature:", np.min(temp))
print("Maximum temperature:", np.max(temp))
print("Mean temperature:", np.mean(temp))
print("Variance:", np.var(temp))
print("Standard Deviation:", np.std(temp))
