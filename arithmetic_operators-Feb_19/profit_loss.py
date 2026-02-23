# ====================================================
# This program does the Profit or Loss Calculation
# ----------------------------------------------------
# Profit = Selling Price - Cost Price
# Loss   = Cost Price - Selling Price
# ====================================================

cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit:", profit)

elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss:", loss)

else:
    print("No Profit No Loss")