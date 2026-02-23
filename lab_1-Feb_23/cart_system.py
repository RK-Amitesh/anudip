"""
Program: E-Commerce Cart System
---------------------------------
- Remove duplicate prices
- Apply 10% discount if total > 5000
- Add 18% GST
- Show final payable amount
"""

GST_RATE = 0.18
DISCOUNT_RATE = 0.10


def process_cart(prices):
    """Process shopping cart pricing."""
    unique_prices = list(set(prices))  # Remove duplicates
    total = sum(unique_prices)

    if total > 5000:
        total -= total * DISCOUNT_RATE

    total += total * GST_RATE
    return round(total, 2)


cart_prices = [1200, 2500, 1200, 1800, 900]

final_amount = process_cart(cart_prices)

print("Final Payable Amount: ₹", final_amount)