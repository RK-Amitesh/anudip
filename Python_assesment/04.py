# Q4. Write a menu-driven banking application using a while loop
# that allows users to deposit, withdraw, check balance,
# and exit only when the user chooses the exit option.

balance = 1000

while True:

    print("\n----- Banking Menu -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice : "))

    # deposit
    if choice == 1:

        amount = int(input("Enter amount to deposit : "))
        balance = balance + amount

        print("Amount Deposited Successfully")
        print("Current Balance =", balance)

    # withdraw
    elif choice == 2:

        amount = int(input("Enter amount to withdraw : "))

        if amount <= balance:

            balance = balance - amount
            print("Amount Withdrawn Successfully")
            print("Current Balance =", balance)

        else:
            print("Insufficient Balance")

    # check balance
    elif choice == 3:

        print("Current Balance =", balance)

    # exit
    elif choice == 4:

        print("Thank You for Using Banking Application")
        break

    else:
        print("Invalid Choice")