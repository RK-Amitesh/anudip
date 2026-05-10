# Q38. Generate random temperature data
# using NumPy and plot a histogram
# representing temperature distribution.

import numpy as np
import matplotlib.pyplot as plt

# generating random temperature data
temperature = np.random.randint(20, 40, 100)

print("Temperature Data :\n")
print(temperature)

# plotting histogram
plt.hist(temperature)

# adding title and labels
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")

# displaying graph
plt.show()