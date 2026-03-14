# Q9
# Generate random numbers and normalize them

import numpy as np

arr = np.random.random(10)

normalized = (arr - arr.min()) / (arr.max() - arr.min())

print(normalized)

# Example Output
# [0.56 0.12 0.95 0.00 0.67 0.42 0.23 0.84 0.71 0.20]