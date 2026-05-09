# Q9. Develop a dictionary-based inventory management system
# where users can add products, update quantity,
# search products, and display low-stock items.

inventory = {}

while True:

    print("\n----- Inventory Menu -----")
    print("1. Add Product")
    print("2. Update Quantity")
    print("3. Search Product")
    print("4. Display Low Stock Items")
    print("5. Exit")

    choice = int(input("Enter your choice : "))

    # add product
    if choice == 1:

        product = input("Enter product name : ")
        qty = int(input("Enter quantity : "))

        inventory[product] = qty

        print("Product Added Successfully")

    # update quantity
    elif choice == 2:

        product = input("Enter product name : ")

        if product in inventory:

            qty = int(input("Enter new quantity : "))
            inventory[product] = qty

            print("Quantity Updated")

        else:
            print("Product Not Found")

    # search product
    elif choice == 3:

        product = input("Enter product name : ")

        if product in inventory:

            print("Product :", product)
            print("Quantity :", inventory[product])

        else:
            print("Product Not Found")

    # low stock items
    elif choice == 4:

        print("\nLow Stock Items :")

        for i in inventory:

            if inventory[i] < 5:

                print(i, "=", inventory[i])

    # exit
    elif choice == 5:

        print("Exiting Program")
        break

    else:
        print("Invalid Choice")