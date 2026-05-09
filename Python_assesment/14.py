# Q14. Create a line chart using Matplotlib
# to display monthly sales data of a company.
# Add title, labels, legend, and grid
# for better visualization.

import matplotlib.pyplot as plt

# monthly sales data
months = ["Jan", "Feb", "Mar", "Apr",
        "May", "Jun"]

sales = [12000, 15000, 18000,
        14000, 20000, 22000]

# plotting line chart
plt.plot(months, sales,
        marker="o",
        label="Monthly Sales")

# title and labels
plt.title("Company Monthly Sales Data")
plt.xlabel("Months")
plt.ylabel("Sales")

# legend and grid
plt.legend()
plt.grid()

# displaying chart
plt.show()