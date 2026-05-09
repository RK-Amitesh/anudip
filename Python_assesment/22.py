# Q22. Read sales data from a CSV file using Pandas
# and plot a bar chart representing product-wise sales
# using Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

# reading csv file
data = pd.read_csv("sales_data.csv")

print("Sales Data :\n")
print(data)

# plotting bar chart
plt.bar(data["Product"], data["Sales"])

# adding title and labels
plt.title("Product-wise Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

# displaying graph
plt.show()