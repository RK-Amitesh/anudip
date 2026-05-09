# Q31. Plot a pie chart showing market share
# of different smartphone brands and highlight
# the brand with maximum market share.

import matplotlib.pyplot as plt

# smartphone brands and market share
brands = ["Samsung", "Apple", "Xiaomi", "OnePlus"]

share = [40, 30, 20, 10]

# highlighting maximum market share
explode = [0.1, 0, 0, 0]

# plotting pie chart
plt.pie(
    share,
    labels=brands,
    explode=explode,
    autopct="%1.1f%%"
)

# title
plt.title("Smartphone Market Share")

# displaying chart
plt.show()