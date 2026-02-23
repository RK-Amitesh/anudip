"""
Program: Inventory Management
---------------------------------
- Remove items with 0 stock
- Add 50 units if stock < 10
- Calculate total inventory
"""

def manage_inventory(stock_list):
    filtered = [s for s in stock_list if s > 0]

    restocked = [
        s + 50 if s < 10 else s
        for s in filtered
    ]

    total_inventory = sum(restocked)
    return restocked, total_inventory


stock = [0, 5, 12, 8, 25]

updated_stock, total = manage_inventory(stock)

print("Updated Stock:", updated_stock)
print("Total Inventory:", total)