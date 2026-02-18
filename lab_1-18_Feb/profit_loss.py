# program to calculate profit or loss
# input of cost price and selling price

cost_price = float(input("Enter the cost price: "))

# validating whether cost price is valid or not
if(cost_price <= 0):
    print("Invalid cost price")
    exit()   # exiting the program if cost price is invalid
else:
    selling_price = float(input("Enter the selling price: "))
    
    # validating whether selling price is valid or not
    if(selling_price <= 0):
        print("Invalid selling price")
        exit()   # exiting the program if selling price is invalid
    else:
        # checking profit or loss
        if(selling_price > cost_price):
            profit = selling_price - cost_price
            print("Profit =", profit)
        
        elif(cost_price > selling_price):
            loss = cost_price - selling_price
            print("Loss =", loss)
        
        else:
            print("No profit, No loss")