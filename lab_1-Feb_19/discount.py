# E-commerce Discount Engine

cart_value = float(input("Enter cart value: "))
membership = input("Enter membership (Silver/Gold/Platinum): ")
festival = input("Is it festival season? (yes/no): ")

discount = 0

# Membership discount
if membership == "silver":
    discount = 5
elif membership == "gold":
    discount = 10
elif membership == "platinum":
    discount = 15

# Cart value discount
if cart_value >= 20000:
    discount = max(discount, 20)
elif cart_value >= 10000:
    discount = max(discount, 10)
elif cart_value >= 5000:
    discount = max(discount, 5)

# Festival discount
if festival == "yes":
    discount = max(discount, 12)

# Final calculation
discount_amount = (cart_value * discount) / 100
final_amount = cart_value - discount_amount

print("Highest Discount Applied:", discount, "%")
print("Final Payable Amount: Rs", final_amount)